from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class AsiaeCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"아시아경제",
            "scope":[
                "view.asiae.co.kr"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
                
        doc=lxml.html.fromstring(html)

        ele=doc.cssselect('.article')[0]

        for bad in ele.cssselect('.article_head, .e_article, .e_article ~ *,'
            'script, div[class^="ad_"], div[class^="dablewidget"], .article_photo, .article_ad, .add_middle'):
            bad.getparent().remove(bad)
        for br in doc.xpath("*//br"):
            br.tail = "\n" + br.tail if br.tail else "\n"

        text=ele.text_content()
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://view.asiae.co.kr/article/2023033115065594764"
    cl=AsiaeCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
