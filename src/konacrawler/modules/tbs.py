from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml
import re

@kcc.register_module
class TbsnewsCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"tbs 뉴스",
            "scope":[
                "tbs.seoul.kr"
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

        ele=doc.cssselect("#sub-center > div.sub1-left-right.div-top35.clearfix > div.left > div.line-bm > ul:nth-child(2) > li")[0]
        text=ele.text_content().strip()
        # text = re.sub(r'◀.+▶', '', text)

        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="http://tbs.seoul.kr/news/bunya.do?method=daum_html2&typ_800=9&idx_800=3421065&seq_800=20413642"
    cl=TbsnewsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
