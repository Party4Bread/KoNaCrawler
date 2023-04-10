from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class SkyedailyCrawler(Knabs1Crawler):
    rm_sel='figure:has(>img), div>span:only-child'
    br_nl=False
    p_nl=False
    cont_sel='#gisaview'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"skyedaily",
            "scope":[
                "skyedaily.com"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://skyedaily.com/news/news_view.html?ID=122032"
    cl=SkyedailyCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
