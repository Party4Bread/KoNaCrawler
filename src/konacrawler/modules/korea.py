from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class KoreaCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"정책브리핑",
            "scope":[
                "www.korea.kr",
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

        # for bad in doc.cssselect('#viewCont > div, .remark'):
        #     bad.getparent().remove(bad)

        ele=doc.cssselect("#viewCont>p")
        text='\n'.join(i.text_content() for i in ele).strip()
        # text=ele.text_content().strip()
        # text = re.sub(r'◀.+▶', '', text)

        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="https://www.korea.kr/news/actuallyView.do?newsId=148861424&call_from=naver_news"
    cl=KoreaCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
