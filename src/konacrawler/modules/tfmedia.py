from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp

@kcc.register_module
class TfmediaCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"조세금융신문",
            "scope":[
                "tfmedia.co.kr",
                "www.tfmedia.co.kr",
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()

        sele=parsel.Selector(html)
        text_p = sele.css('#news_body_area > p')
        text="\n".join(["".join(i.xpath(".//text()").extract()) for i in text_p])
        return text.strip().replace('\n\n', '\n')

if __name__ == "__main__":
    import asyncio
    url="https://tfmedia.co.kr/news/article.html?no=31183"
    cl=TfmediaCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
