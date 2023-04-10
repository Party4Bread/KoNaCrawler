from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class EtodayCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"BizEnter",
            "scope":[
                "enter.etoday.co.kr"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()

        doc=lxml.html.fromstring(html)

        # for bad in doc.cssselect('#ct > p > span'):
        #     bad.getparent().remove(bad)
        
        ele=doc.cssselect("#articleBody > p")
        text='\n'.join(i.text_content() for i in ele)
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="http://enter.etoday.co.kr/news/view/196357"
    cl=EtodayCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
    