from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class SmartfnCrawler(Knabs1Crawler):
    rm_sel='.content>div, script'
    br_nl=False
    p_nl=False
    cont_sel='.content'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"스마트에프엔",
            "scope":[
                "www.smartfn.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="http://www.smartfn.co.kr/article/view/sfn202101290066"
    cl=SmartfnCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
