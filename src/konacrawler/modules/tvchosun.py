from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class TVChosunCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"TV chosun",
            "scope":[
                "news.tvchosun.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
                
        doc=lxml.html.fromstring(html)
        for bad in doc.cssselect('.article_img'):
            bad.getparent().remove(bad)
        ele=doc.cssselect(".article")[0]
        text=ele.text_content()
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="http://news.tvchosun.com/site/data/html_dir/2023/04/04/2023040490128.html"
    cl=TVChosunCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
