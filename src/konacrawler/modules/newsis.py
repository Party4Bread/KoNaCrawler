from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class NewsisCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"뉴시스",
            "scope":[
                "www.newsis.com",
                "newsis.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
                
        doc=lxml.html.fromstring(html)

        ele=doc.cssselect('.viewer > article')[0]
        for bad in ele.cssselect('.summury, #view_ad, .thumCont, script, .iwmads'):
            bad.getparent().remove(bad)
        for br in ele.xpath("*//br"):
            br.tail = "\n" + br.tail if br.tail else "\n"
        text=ele.text_content()
        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://newsis.com/view/?id=NISX20230403_0002251299&cID=10809&pID=10800"
    cl=NewsisCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
