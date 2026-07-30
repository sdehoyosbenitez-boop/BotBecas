import httpx
async def get(url):
    async with httpx.AsyncClient() as c:
        return await c.get(url)
