# Milton Cassul Miranda
import random
import socket
from socket import *

# UDP socket, sua criação

serverSocket = socket(AF_INET, SOCK_DGRAM) # 	SOCK_DGRAM do UDP packets
serverSocket.bind(("127.0.0.1", 8000))	# colocar um endereço  IP e a port number no socket

while True:
	
	rand = random.randint(0, 10)	# gera um numero aleatorio de  0 a 10
	menssage, adress = serverSocket.recvfrom(1024)	# recebe os packeges do client com o endereço de origem
	menssage = menssage.upper()		# recebe a mensagem do cient

	if rand < 4:	# Se a condição for verdadeira, consideramos o pacote perdido e sem resposta
		continue
	serverSocket.sendto(message, adress)	# Senão, o servidor responde