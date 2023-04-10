from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class HeraldCorpCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"해럴드경제",
            "scope":[
                "news.heraldcorp.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
                
        doc=lxml.html.fromstring(html)

        ele=doc.cssselect('#articleText')[0]
        for br in ele.xpath("//br"):
            br.tail = "\n" + br.tail if br.tail else "\n"
        text=ele.text_content()
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="http://news.heraldcorp.com/view.php?ud=20161218000161"
    cl=HeraldCorpCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
