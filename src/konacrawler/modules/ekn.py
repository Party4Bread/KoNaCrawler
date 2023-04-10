from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class SportsseoulCrawler(Knabs1Crawler):
    rm_sel='table'
    br_nl=True
    p_nl=False
    cont_sel='#news_body_area_contents'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"에너지경제",
            "scope":[
                "www.ekn.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.ekn.kr/web/view.php?key=20230404010000813"
    cl=SportsseoulCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
