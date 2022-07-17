import websocket
import brotli
import json
import re
def lookup(nickname: str):
    ws = websocket.create_connection("wss://arc.estertion.win:616/")
    ws.send("lookup " + nickname)
    backMessage = ""
    while backMessage != "bye":
        backMessage = ws.recv()
        if type(backMessage) == type(b''):
            messageJson = json.loads(str(brotli.decompress(backMessage), encoding='utf-8'))
            id = messageJson['data'][0]['code']
            return messageJson
def getInfo(id: str):
    ws = websocket.create_connection("wss://arc.estertion.win:616/")
    ws.send(id)
    backMessage = ""
    while backMessage != "bye":
        try:
            backMessage = ws.recv()
        except websocket._exceptions.WebSocketConnectionClosedException:
            ws = websocket.create_connection("wss://arc.estertion.win:616/")
            ws.send(lookup(id))
        if type(backMessage) == type(b''):
            messageJson = json.loads(str(brotli.decompress(backMessage), encoding='utf-8'))
    return messageJson
def verifyUsercode(id:str):
    pass