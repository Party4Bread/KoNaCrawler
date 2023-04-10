from typing import TypeVar, TypedDict
import konacrawler.core as kcc
import parsel
import aiohttp
import lxml
import abc

class Knabs1Crawler(kcc.KNCRModule,abc.ABC):
    rm_sel=None
    br_nl=False
    p_nl=False
    cont_sel=""
    
    
    async def crawl(self, url: str) -> str:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()

        doc=lxml.html.fromstring(html)

        ele=doc.cssselect(self.cont_sel)[0]

        if self.br_nl:
            for br in doc.xpath("*//br"):
                br.tail = "\n" + br.tail if br.tail else "\n"
        if self.p_nl:
            for br in doc.xpath("*//br"):
                br.tail = "\n" + br.tail if br.tail else "\n"

        if self.rm_sel:
            for bad in doc.cssselect(self.rm_sel):
                bad.getparent().remove(bad)

        text=ele.text_content().strip()
        
        return text.strip()

