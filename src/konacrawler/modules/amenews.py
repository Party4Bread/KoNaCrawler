from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp

@kcc.register_module
class AmenewsCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"신소재경제",
            "scope":[
                "amenews.kr"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()

        sele=parsel.Selector(html)
        text_p = sele.css('#viewContent>p')
        text="\n".join(["".join(i.xpath(".//text()").extract()) for i in text_p])
        return text.replace('\n\n', '\n').replace('  ', ' ')

if __name__ == "__main__":
    import asyncio
    url="http://amenews.kr/news/view.php?idx=53165"
    cl=AmenewsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
