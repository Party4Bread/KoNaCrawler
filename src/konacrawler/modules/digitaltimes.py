from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class DTCrawler(Knabs1Crawler):
    rm_sel='div:has(> img), iframe, center, .article_view>div'
    br_nl=False
    p_nl=False
    cont_sel='.article_view'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"디지털타임즈",
            "scope":[
                "www.dt.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="http://www.dt.co.kr/contents.html?article_no=2023021602109919036008&ref=naver"
    cl=DTCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
