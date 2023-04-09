import konacrawler.core as kcc
from pathlib import Path
import asyncio

kcc.import_modules()
el=asyncio.get_event_loop()
print(kcc.registry.model_entrypoints)

for i in kcc.registry.model_entrypoints:
    n=kcc.registry.model_entrypoints[i]
    print(n.info())
for url in (Path(__file__).parent/"test.txt").read_text('u8').splitlines():
    try:
        hj=url[(n:=url.find("://"))+3:url.index("/",n+3)]
        kn=kcc.registry.hosts_to_models[hj]()
        el.run_until_complete(kn.crawl(url))
        print(f"\033[92mSuccess\033[0m on {url}")
    except:
        print(f"\033[91mError\033[0m on {url}")