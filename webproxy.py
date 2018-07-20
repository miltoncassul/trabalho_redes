# Milton Cassul Miranda
import argparse
import sys
import socket
import itertools
from socket import socket as Socket


def main():

    #  Argumentos da linha de comando. Use a porta 8080 por padrão: amplamente usado para proxys
    # e > 1024, então não precisamos de sudo para rodar.
    parser = argparse.ArgumentParser()
    parser.add_argument('--porta', '-p', default=8080, type=int, help='porta para usar')
    args = parser.parse_args()

    # Crie o sockete do servidor (para manipular solicitações tcp usando ipv4), certifique-se
    # é sempre fechado usando a instrução    
    with Socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        # O socket permanece conectado mesmo depois que este script terminar
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind(('', args.port))
        server_socket.listen(1)
        # sem multithread ainda, precisaria configurar atualizações atômicas para dict.
        # Criar um dicionario vazio para páginas em cache
        cache_dict = {}

        print("servidor proxy pronto")

        while True:
            # Aceite a conexão TCP do cliente
            with server_socket.accept()[0] as connection_socket:

    return 0

if __name__ == "__main__":
    sys.exit(main())