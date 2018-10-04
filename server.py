import asyncio
import pathlib
import ssl
import websockets

from helpers.certificate import create_self_signed_cert, CERT_FILE, KEY_FILE

connected_clients = set()


async def server_handler(connection_socket):
    """
    Method used by the server to handle each server
    :param connection_socket: The connection socket with the client
    """

    if connection_socket not in connected_clients:  # check if first time for client (socket)
        connected_clients.add(connection_socket)



if __name__ == '__main__':
    create_self_signed_cert()  # generate self sign certificate

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)  # specify the protocol version

    ssl_context.load_cert_chain(
        pathlib.Path(__file__).with_name(CERT_FILE),
        keyfile=KEY_FILE
    )  # load the self signed certificate as well as the private key

    server = websockets.serve(server_handler, 'localhost', 9_999, ssl=ssl_context)  # create server

    asyncio.get_event_loop().run_until_complete(server)  # run server
    asyncio.get_event_loop().run_forever()  # keep running server forever
