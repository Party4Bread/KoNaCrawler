from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class AsiatimeCrawler(Knabs1Crawler):
    rm_sel='figure, script,.article_txt_container > div> div'
    br_nl=True
    p_nl=False
    cont_sel='.article_txt_container > div'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"아시아타임즈",
            "scope":[
                "www.asiatime.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.asiatime.co.kr/article/20230302500241"
    cl=AsiatimeCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
