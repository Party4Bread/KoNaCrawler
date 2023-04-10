from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class TechholicCrawler(Knabs1Crawler):
    rm_sel='table, p:nth-last-child(-n+4)'
    br_nl=False
    p_nl=False
    cont_sel='#articleBody'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"techholic",
            "scope":[
                "www.techholic.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="http://www.techholic.co.kr/news/articleView.html?idxno=202414#rs"
    cl=TechholicCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
