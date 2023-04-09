from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp

@kcc.register_module
class Viva100Crawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"브릿지경제",
            "scope":[
                "www.viva100.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()

        sele=parsel.Selector(html)
        text_p = sele.css('#container > div.con_left > div.view_left_warp > div.left_text_box > p')
        text="\n".join(["\n".join(i.xpath(".//text()").extract()) for i in text_p])
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://www.viva100.com/main/view.php?key=20230205010001190"
    cl=Viva100Crawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
