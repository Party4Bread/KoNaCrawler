from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class JoongdoCrawler(Knabs1Crawler):
    rm_sel='.cont-area>div'
    br_nl=True
    p_nl=False
    cont_sel='.cont-area'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"한국정경신문",
            "scope":[
                "kpenews.com"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="http://kpenews.com/View.aspx?No=53810"
    cl=JoongdoCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
