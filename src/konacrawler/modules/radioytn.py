from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class radioYTNCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"ytn라디오",
            "scope":[
                "radio.ytn.co.kr"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
                
        doc=lxml.html.fromstring(html)

        toDelete = ['.content_area > h2', '.content_area > script', '.content_area > div', '.content_area > thead']

        for selector in toDelete:
            for bad in doc.cssselect(selector):
                bad.getparent().remove(bad)
        
        ele=doc.cssselect(".content_area")[0]
        text=ele.text_content()
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://radio.ytn.co.kr/program/?f=2&id=76191&s_mcd=0214&s_hcd=01"
    cl=radioYTNCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
