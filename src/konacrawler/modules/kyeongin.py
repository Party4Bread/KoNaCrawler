from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml

@kcc.register_module
class KyeonginCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"경인일보",
            "scope":[
                "www.kyeongin.com",
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

        # for bad in doc.cssselect('#articleBody>div, #articleBody>style, #articleBody>iframe,#articleBody>ul'):
        #     bad.getparent().remove(bad)

        ele=doc.cssselect("#font > div > div:nth-child(2) > font")
        text='\n'.join(i.text_content() for i in ele).strip()
        # text=ele.text_content().strip()
        # text = re.sub(r'◀.+▶', '', text)

        return text.strip()

if __name__ == "__main__":
    import asyncio
    url="http://www.kyeongin.com/main/view.php?key=20180128010008405"
    # url = 'https://www.yonhapnewstv.co.kr/news/MYH20230402011900641?input=1825m'
    cl=KyeonginCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
