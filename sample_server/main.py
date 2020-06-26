import datetime
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.post('/log/sample/indoor')
async def log_indoor_sample(request):
    # print("Headers: ", dict(request.headers))
    # print("query parameters: ", dict(request.query))
    if request.body_exists:
        headers = dict(request.headers)
        mac = headers.get('X-MAC', '?')
        body = await request.post()
        sample = dict(body)
        dt = datetime.datetime.now().isoformat()
        row = f"{dt},{mac},{sample['type']},{int(sample['t'])},{int(sample['h'])},{int(sample['p'])},{int(sample['g'])}"
        print(row)
        with open('indoor_sample.csv', 'a') as file:
            file.write(f"{row}\n")        
    return web.Response(text="Received OK, Thanks.")

app = web.Application()
app.add_routes(routes)
web.run_app(app)
