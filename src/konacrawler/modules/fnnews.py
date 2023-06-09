from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class FnNewsCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"파이낸셜뉴스",
            "scope":[
                "www.fnnews.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
                
        doc=lxml.html.fromstring(html)

        ele=doc.cssselect('#article_content')[0]

        for bad in ele.cssselect('.article_head, #customByline, #customByline ~ *,'
            'script, div[class^="ad_"], div[class^="dablewidget"], .article_photo, .article_ad, .art_subtit'):
            bad.getparent().remove(bad)

        text=ele.text_content()
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://www.fnnews.com/news/202303301526040884"
    cl=FnNewsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
