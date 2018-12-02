
import asyncio
import websockets
@asyncio.coroutine
def echo(websocket, path):
 message = yield from websocket.recv()
 print('recv', message)
 server_data = "收到服务端的数据"
 yield from websocket.send(server_data)
start_server = websockets.serve(echo, 'localhost', 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
