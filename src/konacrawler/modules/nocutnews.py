from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class NocutnewsCrawler(Knabs1Crawler):
    rm_sel='#pnlContent>div,#pnlContent>span'
    br_nl=True
    p_nl=False
    cont_sel='#pnlContent'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"노컷뉴스",
            "scope":[
                "www.nocutnews.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.nocutnews.co.kr/news/5921501"
    cl=NocutnewsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
