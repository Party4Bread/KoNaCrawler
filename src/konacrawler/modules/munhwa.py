from typing import TypeVar, TypedDict
import konacrawler.core as kcc
from konacrawler.modules.knabs1 import Knabs1Crawler

@kcc.register_module
class EdailyCrawler(Knabs1Crawler):
    rm_sel='#News_content>p'
    br_nl=False
    p_nl=False
    cont_sel='#News_content'

    @staticmethod
    def info()->kcc.ModuleInfo:
        return {
            "name":"문화일보",
            "scope":[
                "www.munhwa.com",
            ]
        }

if __name__ == "__main__":
    import asyncio
    url = 'https://www.munhwa.com/news/view.html?no=2023033001071227270001'
    
    
    cl=EdailyCrawler()
    
    print(asyncio.get_event_loop().run_until_complete(cl.crawl(url)))
