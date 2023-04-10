from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class SportsseoulCrawler(Knabs1Crawler):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"스포츠서울",
            "scope":[
                "www.sportsseoul.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()

        sele=parsel.Selector(html)
        text_p = sele.css('#article-body>p')
        text="\n".join(["\n".join(i.xpath(".//text()").extract()) for i in text_p])
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://www.sportsseoul.com/news/read/1302650?ref=naver"
    cl=SportsseoulCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
