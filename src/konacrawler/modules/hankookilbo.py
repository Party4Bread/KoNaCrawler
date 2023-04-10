from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class HankookIlboCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"한국일보",
            "scope":[
                "www.hankookilbo.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
                
        doc=lxml.html.fromstring(html)
        for bad in doc.cssselect('.article_img[itemprop="articleBody"], .writer ~ *, .writer, .end-ad-container, .editor-img-box'):
            bad.getparent().remove(bad)
        for br in doc.xpath("*//br"):
            br.tail = "\n" + br.tail if br.tail else "\n"

        ele=doc.cssselect('.col-main[itemprop="articleBody"]')[0]
        text=ele.text_content()
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://www.hankookilbo.com/News/Read/A2023022706210001472?did=NA"
    cl=TVChosunCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
