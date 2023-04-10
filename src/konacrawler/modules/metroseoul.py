from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class MetroseoulCrawler(Knabs1Crawler):
    rm_sel='figure'
    br_nl=False
    p_nl=False
    cont_sel='body > div.container > div.left-container.left-article-txt.layout_sortable > div.row.article-txt-contents > div'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"metroseoul",
            "scope":[
                "www.metroseoul.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.metroseoul.co.kr/article/20230209500089"
    cl=MetroseoulCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
