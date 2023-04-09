from pathlib import Path
import asyncio
from collections import Counter
import aiohttp


async def test(url):
    try:
        headers={"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                html = await resp.text()
        
        return "article-view-content-div" in html
    except:
        return False
    

async def main():
    it = (Path(__file__).parent/"test.txt").read_text('u8').splitlines()
    res=await asyncio.gather(*(asyncio.ensure_future(test(url))for url in it))
    print(Counter(res))
        

asyncio.run(main())