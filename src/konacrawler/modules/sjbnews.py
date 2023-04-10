from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class AjuNewsCrawler(Knabs1Crawler):
    rm_sel=''
    br_nl=False
    p_nl=False
    cont_sel='.news_text'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"새전북뉴스",
            "scope":[
                "sjbnews.com"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="http://sjbnews.com/news/news.php?number=774866"
    cl=AjuNewsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
