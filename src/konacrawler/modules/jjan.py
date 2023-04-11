from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class JjanCrawler(Knabs1Crawler):
    rm_sel='script, .article_txt_container>div:has(>div),.article_txt_container>div:has(>figure), .article_txt_container>figure, table, .arti_copy'
    br_nl=False
    p_nl=True
    cont_sel='.article_txt_container'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"전북일보",
            "scope":[
                "www.jjan.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="http://www.jjan.kr/2126501"
    cl=JjanCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
