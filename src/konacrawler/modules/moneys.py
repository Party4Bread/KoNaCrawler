from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class MoneysCrawler(Knabs1Crawler):
    rm_sel='#textBody>div>div, #textBody>div>table'
    br_nl=True
    p_nl=False
    cont_sel='#textBody>div'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"moneys",
            "scope":[
                "moneys.mt.co.kr"
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
    url='https://moneys.mt.co.kr/news/mwView.php?no=2023040518081129672'
    cl=MoneysCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
