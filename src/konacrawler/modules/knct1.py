from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp

@kcc.register_module
class KnCT1Crawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"언론사 일반 템플릿 1",
            "scope":[
                "weekly.chosun.com","news.unn.net",
                "www.dtnews24.com", "weekly.chosun.com",
                "news.unn.net", "www.incheonin.com", 
                "www.fsnews.co.kr", "www.ccdailynews.com",
                
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
        sele = parsel.Selector(html)
        text_p = sele.css('#article-view-content-div > p')
        text="\n".join(["".join(i.xpath(".//text()").extract()) for i in text_p])
        return text

if __name__ == "__main__":
    import asyncio
    url="http://www.fsnews.co.kr/news/articleView.html?idxno=48199"
    cl=KnCT1Crawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
