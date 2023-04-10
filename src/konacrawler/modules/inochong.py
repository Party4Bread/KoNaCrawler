from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class InochongCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"노동과희망",
            "scope":[
                "news.inochong.org"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()

        doc=lxml.html.fromstring(html)

        for bad in doc.cssselect('#ct > p > span'):
            bad.getparent().remove(bad)
        
        ele=doc.cssselect("#ct > p")
        text='\n'.join(i.text_content() for i in ele)
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="http://news.inochong.org/detail.php?number=4638&thread=22r07"
    cl=InochongCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
