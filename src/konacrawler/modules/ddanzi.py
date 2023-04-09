from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class DdanziCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"딴지일보",
            "scope":[
                "www.ddanzi.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
                
        doc=lxml.html.fromstring(html)
        for bad in doc.cssselect('p > strong > span > img'):
            p=(n:=bad.getparent().getparent().getparent()).getparent()
            p.remove(n.getnext())
            p.remove(n)

        for bad in doc.cssselect('p img'):
            p=(n:=bad.getparent()).getparent()
            p.remove(n.getnext())
            p.remove(n)

        ele=doc.cssselect(".read_content")[0]
        text=ele.text_content()
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://www.ddanzi.com/ddanziNews/765068064"
    cl=DdanziCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
