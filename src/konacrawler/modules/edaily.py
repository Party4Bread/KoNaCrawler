from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class EdailyCrawler(Knabs1Crawler):
    rm_sel='.news_body>table'
    br_nl=True
    p_nl=False
    cont_sel='.news_body'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"이데일리",
            "scope":[
                "www.edaily.co.kr",
            ]
        }

if __name__ == "__main__":
    import asyncio
    url='https://www.edaily.co.kr/news/read?newsId=02607606635572840&mediaCodeNo=257&OutLnkChk=Y'
    cl=EdailyCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
