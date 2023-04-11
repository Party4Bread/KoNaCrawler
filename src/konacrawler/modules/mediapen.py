from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class CrawIfsler(Knabs1Crawler):
    rm_sel='#articleBody>a, #articleBody>div:has(>table)'
    br_nl=True
    p_nl=True
    cont_sel='#articleBody'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"mediapen",
            "scope":[
                "www.mediapen.com"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="http://www.mediapen.com/news/view/791226"
    cl=CrawIfsler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
