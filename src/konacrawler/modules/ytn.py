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
    cont_sel='#CmAdContent'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"ytn",
            "scope":[
                "www.ytn.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.ytn.co.kr/_ln/0101_202104201454077777"
    cl=JibsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
