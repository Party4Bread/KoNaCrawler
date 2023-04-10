from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class KoreadailyCrawler(Knabs1Crawler):
    rm_sel='#article_body>div, h1'
    br_nl=True
    p_nl=False
    cont_sel='#article_body'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"중앙일보",
            "scope":[
                "news.koreadaily.com"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://news.koreadaily.com/2023/04/06/society/generalsociety/20230406151100427.html"
    cl=KoreadailyCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
