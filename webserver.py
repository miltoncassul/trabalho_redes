# Milton Cassul Miranda
import argparse
import sys
import itertools
import socket
from socket import socket as Socket


def main():

    # Argumentos da linha de comando. Use uma porta 1024 por padrão para poder executar
    # Sem root, para usar como um servidor real, é precisa usar a porta 80.
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', default=2080, type=int,
                        help='Port to use')
    args = parser.parse_args()

    # Crie o soquete do servidor (para manipular solicitações tcp usando ipv4), certifica
    with Socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        # O soquete permanece conectado mesmo depois que esse script termina. Então, a fim para permitir a reutilização imediata do socket
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', args.port))
        server_socket.listen(1)

        print("server ready")

        while True:

            with server_socket.accept()[0] as connection_socket:
                request = connection_socket.recv(1024).decode('ascii')
                reply = http_handle(request)
                connection_socket.send(reply.encode('ascii'))

            print("\n\nPedido Recebido")
            print("======================")
            print(request.rstrip())
            print("======================")

            print("\n\nRespondido Com")
            print("======================")
            print(reply.rstrip())
            print("======================")

    return 0

def http_handle(request_string):
    """ 
        Dada uma solicitação http, retorne uma resposta 
        tanto a solicitação quanto a resposta são strings unicode com padrão de plataforma
        terminações de linha.
    """
    assert not isinstance(request_string, bytes)
    # Preencha o código para manipular a solicitação http.
    raise NotImplementedError
    pass

if __name__ == "__main__":
    sys.exit(main())