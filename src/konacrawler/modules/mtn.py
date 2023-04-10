from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class MtnCrawler(Knabs1Crawler):
    rm_sel='figure'
    br_nl=True
    p_nl=False
    cont_sel='.news-content'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"mtn",
            "scope":[
                "news.mtn.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://news.mtn.co.kr/news-detail/2023040706064339247"
    cl=MtnCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
