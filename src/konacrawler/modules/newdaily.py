from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class JoongdoCrawler(Knabs1Crawler):
    rm_sel='#article_conent>iframe, script, #article_conent>div:has(>img)'
    br_nl=True
    p_nl=False
    cont_sel='#article_conent'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"newdaily",
            "scope":[
                "www.newdaily.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.newdaily.co.kr/site/data/html/2023/02/16/2023021600223.html"
    cl=JoongdoCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
