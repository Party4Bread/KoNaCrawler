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
                "www.pinpointnews.co.kr", "www.incheonin.com", "www.idaegu.co.kr", 
                "www.seoulfn.com", "www.pennmike.com", "www.kdfnews.com", 
                "www.thelec.kr", "www.100ssd.co.kr", "www.fsnews.co.kr", 
                "www.kihoilbo.co.kr", "www.mediatoday.co.kr", "www.paxetv.com", 
                "www.womennews.co.kr", "www.topstarnews.net", "www.ccnnews.co.kr", 
                "www.hellodd.com", "www.daejonilbo.com", "www.m-i.kr", "www.jbnews.com", 
                "www.shinailbo.co.kr", "www.dailypop.kr", "www.ksilbo.co.kr", 
                "www.kyongbuk.co.kr", "www.newscj.com", "daily.hankooki.com", 
                "www.polinews.co.kr", "news.lghellovision.net", "www.sportsq.co.kr", 
                "www.e2news.com", "www.domin.co.kr", "www.cstimes.com", "www.ccdailynews.com", 
                "www.sisajournal.com", "www.gndomin.com", "www.veritas-a.com", 
                "www.ltn.kr", "www.jejusori.net", "weekly.chosun.com", 
                "www.gnmaeil.com", "www.onews.tv", "www.womentimes.co.kr", 
                "www.electimes.com", "www.labortoday.co.kr", "www.dkilbo.com", 
                "www.idomin.com", "www.newsfreezone.co.kr", "www.newscape.co.kr", 
                "www.catholicnews.co.kr", "www.dtnews24.com", "news.bbsi.co.kr", 
                "www.ggilbo.com", "www.farminsight.net", "www.sisafocus.co.kr", 
                "www.srtimes.kr", "www.energydaily.co.kr", "www.enewstoday.co.kr", 
                "www.agrinet.co.kr", "www.ftoday.co.kr", "www.ntoday.co.kr", 
                "www.gjdream.com", "www.newspost.kr", "www.thekpm.com", 
                "news.unn.net", "www.goodkyung.com", "www.straightnews.co.kr", 
                "www.gvalley.co.kr", "www.aflnews.co.kr", "www.cctoday.co.kr", 
                "www.kado.net", "www.ilyoseoul.co.kr", "www.greened.kr", 
                "www.cbci.co.kr", "www.ccdn.co.kr", "www.ccdn.co.kr"
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
    url="http://www.pennmike.com/news/articleView.html?idxno=61202"
    cl=KnCT1Crawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
