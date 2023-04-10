from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class SportsseoulCrawler(Knabs1Crawler):
    rm_sel='#news_bodyArea > div'
    br_nl=False
    p_nl=False
    cont_sel='#news_bodyArea'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"청년일보",
            "scope":[
                "www.youthdaily.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.youthdaily.co.kr/news/article.html?no=75532"
    cl=SportsseoulCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
