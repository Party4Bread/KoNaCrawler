import konacrawler.core as kcc
from pathlib import Path
import asyncio

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
        print(f"\033[92mSuccess\033[0m on `{url}` Cont : {res[20:50]}...")
    except Exception as e:
        print(f"\033[91mError\033[0m on `{url}`",e) 

async def main():
    it = (Path(__file__).parent/"test.txt").read_text('u8').splitlines()
    await asyncio.gather(*(asyncio.ensure_future(test(url))for url in it))
        

asyncio.run(main())