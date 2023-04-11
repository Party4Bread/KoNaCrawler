from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler
import parsel
import aiohttp
import lxml

@kcc.register_module
class PnCrawler(Knabs1Crawler):
    rm_sel='#news_body_area>div, #news_body_area>script'
    br_nl=False
    p_nl=False
    cont_sel='#news_body_area'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"이코노미뉴스",
            "scope":[
                "www.m-economynews.com"
            ]
        }
    
    # async def crawl(self, url: str) -> str:
    #     headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
    #     async with aiohttp.ClientSession(headers=headers) as session:
    #         async with session.get(url) as resp:
    #             html = await resp.text()

    #     doc=lxml.html.fromstring(html)

    #     ele=doc.cssselect('#articleBody')[0]

    #     # for bad in ele.cssselect('div[class^="writer-zone"], .photo-group, aside, .related-zone, .txt-copyright, .adrs'):
    #     #     bad.getparent().remove(bad)
    #     # for br in doc.xpath("*//br"):
    #     #     br.tail = "\n" + br.tail if br.tail else "\n"

    #     text=ele.text_content()
    #     return text.strip()

if __name__ == "__main__":
    import asyncio
    url='http://www.m-economynews.com/news/article.html?no=36920'
    cl=PnCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
