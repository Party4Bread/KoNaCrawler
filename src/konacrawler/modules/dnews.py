from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class DnewsCrawler(Knabs1Crawler):
    rm_sel='table, p>strong'
    br_nl=True
    p_nl=False
    cont_sel='.text'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"대한경제",
            "scope":[
                "www.dnews.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.dnews.co.kr/uhtml/view.jsp?idxno=202304050909092580934"
    cl=DnewsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
