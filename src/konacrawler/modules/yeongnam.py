from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class YeongnamCrawler(Knabs1Crawler):
    rm_sel='.article-news_body>table, script'
    br_nl=False
    p_nl=True
    cont_sel='.article-news-body'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"영남일보",
            "scope":[
                "www.yeongnam.com"
            ]
        }
    
    # async def crawl(self, url: str) -> str:
    #     headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
    #     async with aiohttp.ClientSession(headers=headers) as session:
    #         async with session.get(url) as resp:
    #             html = await resp.text()

    #     sele=parsel.Selector(html)
    #     text_p = sele.css('.news_txt')
    #     text = ''.join(['\n'.join(text_p[0].xpath('.//text()')[:-7].extract())])
    #     return text.strip()

if __name__ == "__main__":
    import asyncio
    url='https://www.yeongnam.com/web/view.php?key=20230316010002212'
    cl=YeongnamCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
