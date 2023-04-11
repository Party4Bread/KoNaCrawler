from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp

@kcc.register_module
class KookjeCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"국제신문",
            "scope":[
                "www.kookje.co.kr",
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()

        sele=parsel.Selector(html)
        text_p = sele.css('#news_textArea > div.news_article')
        text="\n".join(["".join(i.xpath(".//text()").extract()) for i in text_p])
        return text.strip().replace('\n\n', '\n')

if __name__ == "__main__":
    import asyncio
    url="http://www.kookje.co.kr/news2011/asp/newsbody.asp?code=1700&key=20230112.22019003127"
    cl=KookjeCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
