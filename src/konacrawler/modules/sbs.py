from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class SbsCrawler(Knabs1Crawler):
    rm_sel='.text_area'
    br_nl=False
    p_nl=False
    cont_sel='.text_area'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"SBS",
            "scope":[
                "news.sbs.co.kr"
            ]
        }
    
    # async def crawl(self, url: str) -> str:
    #     headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
    #     async with aiohttp.ClientSession(headers=headers) as session:
    #         async with session.get(url) as resp:
    #             html = await resp.text()

    #     sele=parsel.Selector(html)
    #     text_p = sele.css('.news_txt')
    #     text = ''.join(['\n'.join(text_p[0].xpath('.//text()')[:-7].extract())])
    #     return text.strip()

if __name__ == "__main__":
    import asyncio
    url='https://news.sbs.co.kr/news/endPage.do?news_id=N1004594911&plink=ORI&cooper=NAVER'
    cl=SbsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
