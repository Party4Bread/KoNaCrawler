from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class MtCrawler(Knabs1Crawler):
    rm_sel='#textBody>table, #textBody>div'
    br_nl=False
    p_nl=False
    cont_sel='#textBody'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"머니투데이",
            "scope":[
                "news.mt.co.kr"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url='https://news.mt.co.kr/mtview.php?no=2023040515144131498'
    cl=MtCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
