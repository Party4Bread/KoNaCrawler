from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class BusinesspostCrawler(Knabs1Crawler):
    rm_sel='#font > table, p'
    br_nl=True
    p_nl=False
    cont_sel='#font'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"joongdo",
            "scope":[
                "www.joongdo.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="http://www.joongdo.co.kr/web/view.php?key=20230406010001797"
    cl=BusinesspostCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
