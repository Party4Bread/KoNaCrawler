import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler

@kcc.register_module
class AjuNewsCrawler(Knabs1Crawler):
    rm_sel='.imgBox, div[class^="dcamp_ad"], .relate_box, .article_bot, .article_bot ~ *, script'
    br_nl=False
    p_nl=False
    cont_sel='#articleBody'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"아주경제",
            "scope":[
                "www.ajunews.com"
            ]
        }

if __name__ == "__main__":
    import asyncio
    url="https://www.ajunews.com/view/20210420133114713"
    cl=AjuNewsCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
