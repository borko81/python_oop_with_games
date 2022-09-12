from aiohttp import web


async def hello(request):
    return web.Response(text='First http server')


async def show_name(request):
    return web.Response(
        text="Hello, {}".format(request.match_info['name'])
    )


async def show_age(request):
    return web.Response(
        text=f'Age is {request.match_info["age"]}'
    )


class Handler:
    def __init__(self):
        pass

    @staticmethod
    async def handle_profile(request):
        name = request.match_info.get('name', 'Anonymous')
        data = {'name': name.upper()}
        return web.json_response(
            data
        )


app = web.Application()
handler = Handler()
app.add_routes([
    web.get('/', hello),
    web.get(r'/name/{name:\w+}', show_name),
    web.get(r'/age/{age:\d+}', show_age),
    web.get(r'/profile/{name}', handler.handle_profile)
])

web.run_app(app, port=8888)
