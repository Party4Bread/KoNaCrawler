from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class OhmynewsCrawler(Knabs1Crawler):
    rm_sel='.at_contents>table, .at_contents>div'
    br_nl=True
    p_nl=False
    cont_sel='.at_contents'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"오마이뉴스",
            "scope":[
                "www.ohmynews.com",
            ]
        }

if __name__ == "__main__":
    import asyncio
    url='https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0002916960&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news'
    cl=OhmynewsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
