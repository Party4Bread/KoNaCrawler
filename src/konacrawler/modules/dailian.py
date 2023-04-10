from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class DailianCrawler(Knabs1Crawler):
    rm_sel='.article>div, script'
    br_nl=True
    p_nl=False
    cont_sel='.article'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"데일리안",
            "scope":[
                "www.dailian.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.dailian.co.kr/news/view/1207290/?sc=Naver"
    cl=DailianCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
