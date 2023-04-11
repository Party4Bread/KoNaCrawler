from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class PnCrawler(Knabs1Crawler):
    rm_sel='#jose_news_view>div>div.caption, p.view_subtle'
    br_nl=False
    p_nl=False
    cont_sel='#jose_news_view>div'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"조세일보",
            "scope":[
                "www.joseilbo.com",
            ]
        }

if __name__ == "__main__":
    import asyncio
    url='http://www.joseilbo.com/news/htmls/2023/02/20230212478162.html'
    cl=PnCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
