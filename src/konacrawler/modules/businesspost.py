from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class BusinesspostCrawler(Knabs1Crawler):
    rm_sel='.detail_editor > div > div'
    br_nl=False
    p_nl=False
    cont_sel='.detail_editor > div'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"businesspost",
            "scope":[
                "www.businesspost.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.businesspost.co.kr/BP?command=article_view&num=233676"
    cl=BusinesspostCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
