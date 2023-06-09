from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class SmartfnCrawler(Knabs1Crawler):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"매일신문",
            "scope":[
                "news.imaeil.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()

        doc=lxml.html.fromstring(html)

        for bad in doc.cssselect('#articlebody>div, figure'):
            bad.getparent().remove(bad)

        ele=doc.cssselect("#articlebody")[0]
        text=ele.text_content().strip().replace('.', '.\n')

        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://news.imaeil.com/page/view/2023031611461773862"
    cl=SmartfnCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
