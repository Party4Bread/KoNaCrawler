from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class JibsCrawler(Knabs1Crawler):
    rm_sel='#print-div-content > div>div, strong'
    br_nl=True
    p_nl=False
    cont_sel='#print-div-content > div'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"jibs",
            "scope":[
                "www.jibs.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="http://www.jibs.co.kr/news/articles/articlesDetail/29665?feed=na"
    cl=JibsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
