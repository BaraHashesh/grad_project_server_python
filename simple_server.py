import asyncio
import pathlib
import ssl
import websockets
from helpers.certificate import create_self_signed_cert

clients = set()


async def hello(connection_socket, path):

    if connection_socket not in clients:
        clients.add(connection_socket)

    name = await connection_socket.recv()

    print(connection_socket)

    print(f"< {name}")

    print(type(name))

    greeting = f"Hello {name}!"

    data = await connection_socket.recv()
    print(type(data) is bytes)

    print(data)

    await connection_socket.send(greeting)
    print(f"> {greeting}")

    clients_to_remove = set()

    for client in clients:
        if client != connection_socket:
            if client.open:
                await client.send("Hello")
            else:
                clients_to_remove.add(client)

    for client in clients_to_remove:
        clients.remove(client)


if __name__ == '__main__':
    create_self_signed_cert()

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ssl_context.load_cert_chain(
        pathlib.Path(__file__).with_name('self_signed.crt'),
        keyfile="private.key"
    )

    start_server = websockets.serve(hello, 'localhost', 9_999, ssl=ssl_context)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

