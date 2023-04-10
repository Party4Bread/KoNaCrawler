from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml
import re

@kcc.register_module
class Knct2Crawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"mbc 템플릿",
            "scope":[
                "chmbc.co.kr",
                "dgmbc.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()

        doc=lxml.html.fromstring(html)

        for br in doc.xpath("*//br"):
            br.tail = "\n" + br.tail if br.tail else "\n"

        ele=doc.cssselect("#journal_article_wrap")[0]
        text=ele.text_content().strip().replace('\n\n\n\n', '\n').replace('\n\n', '')
        text = re.sub(r'◀.+▶', '', text)

        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://dgmbc.com/article/H9E9ucpdQfxXzbCtUfk9C7"
    cl=Knct2Crawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
