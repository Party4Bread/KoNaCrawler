import argparse
import json
import konacrawler.core as kcc
import platform
import asyncio
import logging
from tqdm.asyncio import tqdm_asyncio

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
async def test(url):
    try:
        hj=url[(n:=url.find("://"))+3:url.index("/",n+3)]

        kn=kcc.registry.hosts_to_models[hj]()
        
        res = await kn.crawl(url)
        return {"text":res,"url":url}
    except Exception as e:
        return {"text":False,"url":url}

        

async def main(args):
    kcc.import_modules(args.custom_module)
    with open(args.infile,"r") as infile, \
        open(args.outfile,"w+",encoding='u8') as outfile:
        urls=infile.readlines()
        results=await tqdm_asyncio.gather(*(asyncio.ensure_future(test(url.strip())) for url in urls))
        for result in results:
            json.dump(result,outfile,ensure_ascii=False)
            outfile.write('\n')


if __name__=="__main__":
    parser = argparse.ArgumentParser(
                        prog='KoNaCrawler',
                        description='Korean News article Crawler')
    
    parser.add_argument('infile')
    parser.add_argument('outfile')
    parser.add_argument('--custom_module', required=False)
    args = parser.parse_args()
    asyncio.run(main(args))
