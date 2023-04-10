import konacrawler.core as kcc
from pathlib import Path
import asyncio
from collections import Counter

kcc.import_modules()
el=asyncio.get_event_loop()
print(kcc.registry.model_entrypoints)

for i in kcc.registry.model_entrypoints:
    n=kcc.registry.model_entrypoints[i]
    print(n.info())

async def test(url):
    try:
        hj=url[(n:=url.find("://"))+3:url.index("/",n+3)]
        kn=kcc.registry.hosts_to_models[hj]()
        
        res = await kn.crawl(url)
        prev=res[20:50].replace('\n',' ')
        print(f"\033[92mSuccess\033[0m on `{url}` Cont : {prev}...")
        return True
    except Exception as e:
        print(f"\033[91mError\033[0m on `{url}`",e) 
        return False

async def main():
    it = (Path(__file__).parent/"test.txt").read_text('u8').splitlines()
    res=await asyncio.gather(*(asyncio.ensure_future(test(url))for url in it))
    print(Counter(res))
        
import platform
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())