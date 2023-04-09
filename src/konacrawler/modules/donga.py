from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class DongaCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"동아일보",
            "scope":[
                "www.donga.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
        #sele = parsel.Selector(html)
        #text_p = sele.css('#article_txt a, #article_txt b, #article_txt p, #article_txt')
        doc=lxml.html.fromstring(html)
        for br in doc.xpath("*//br"):
            br.tail = "\n" + br.tail if br.tail else "\n"
        for bad in doc.cssselect('.article_issue, div[class^="view_ads"], div[class^="articlePhoto"]'):
            bad.getparent().remove(bad) 
        ele=doc.cssselect("#article_txt")[0]
        text=ele.text_content()
        text=text[:text.find("function getPoll()")]
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://www.donga.com/news/Opinion/article/all/20230404/118685233/1"
    cl=DongaCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
