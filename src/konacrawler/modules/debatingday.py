from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml
import json

@kcc.register_module
class DebatingdayCrawler(kcc.KNCRModule):
    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"디베이팅 데이",
            "scope":[
                "debatingday.com"
            ]
        }
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
                
        doc=lxml.html.fromstring(html)

        ele=doc.cssselect('#content>div')[0]

        # for bad in ele.cssselect():
        #     bad.getparent().remove(bad)
        # for br in doc.xpath("*//br"):
        #     br.tail = "\n" + br.tail if br.tail else "\n"
        
        res = {
            'title': '',
            'discussion': '',
            'news': [],
            'pros opinion': [],
            'cons opinion': [],
            'opinions': []
        }
        
        res['title'] = ele.cssselect('.entry-title>span')[0].text_content()
        res['discussion'] = ele.cssselect('#contexts>div>p')[0].text_content()
        for news in ele.cssselect('#contexts>div>div>p:has(a)'):
            for n in news.text_content().split('\n'):
                res['news'].append(n)
        
        prosAndcons = ele.cssselect('#contexts>div>div>p:has(strong)')
        try:
            res['pros opinion'] = [prosAndcons[0].text_content().strip(), prosAndcons[1].text_content().strip()]
            res['cons opinion'] = [prosAndcons[2].text_content().strip(), prosAndcons[3].text_content().strip()]
        except:
            pass
        
        for op in ele.cssselect('div.message'):
            opin = {
                'side': '',
                'text': '',
                'thumbs-up': '',
                'thumbs-down': '',
            }
            for s in op.cssselect('.label'):
                opin['side'] = s.text_content()

            for o in op.cssselect('p'):
                opin['text'] += o.text_content()
                
            for up in op.cssselect('.uss'):
                opin['thumbs-up'] += up.text_content()
            for down in op.cssselect('.dss'):
                opin['thumbs-down'] += down.text_content()

            if opin['side'] == '':
                opin['side'] = '중립'

            res['opinions'].append(opin)
        
        return json.dumps(res)

if __name__ == "__main__":
    import asyncio
    url="https://debatingday.com/22426/%ed%96%a5%ed%9b%84-%ec%9e%90%ec%9c%a8-%ec%a3%bc%ed%96%89%ec%9d%b4-%eb%b3%b4%ea%b8%89%eb%90%a0-%ea%b2%bd%ec%9a%b0-%ec%9a%b4%ec%a0%84%eb%a9%b4%ed%97%88%eb%8a%94-%ed%95%84%ec%88%98%ec%9d%b8%ea%b0%80/"
    cl=DebatingdayCrawler()
    
    res = asyncio.get_event_loop().run_until_complete(cl.crawl(url))
    print(json.loads(res))