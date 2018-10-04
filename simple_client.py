#!/usr/bin/env python
import json
import os
import ssl
import time

import websockets
from time import sleep

from helpers.json_parser import to_json, from_json
from models.basic_file_data import BasicFileData as File
from datetime import datetime

from models.message import Message

ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)


async def hello():
    async with websockets.connect('wss://localhost:9999',
                                  ssl=ssl_context) as connection_socket:
        name = input("What's your name? ")

        await connection_socket.send(name)
        print(f"> {name}")

        if name == 'wait':
            sleep(10)

        await connection_socket.send(b'010101')

        greeting = await connection_socket.recv()
        print(f"< {greeting}")


file = File("./venv")

print(to_json(file))

print(from_json(to_json(file), File))

# asyncio.get_event_loop().run_until_complete(hello())
