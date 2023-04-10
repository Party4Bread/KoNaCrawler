from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class KgnewsCrawler(Knabs1Crawler):
    rm_sel=''
    br_nl=False
    p_nl=False
    cont_sel='#news_body_area'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"경기신문",
            "scope":[
                "www.kgnews.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.kgnews.co.kr/news/article.html?no=657463"
    cl=KgnewsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
