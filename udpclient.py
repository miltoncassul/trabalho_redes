# Milton Cassul Miranda
from socket import AF_INET, SOCK_DGRAM
import time

print ("Funcionando Bem") # Informa se o programa foi iniciado corretamente

serverName = ("127.0.0.1") # Conjunto de servidores como ip geral do computador
clientSocket = socket.socket(AF_INET,SOCK_DGRAM) # Cria um socket
clientSocket.settimeout(1) # Define o tempo limite em 1 segundo
num_seq = 1 # Acompanha o número de sequência

while num_seq<=10:
	menssage = ("Ping") # Menssage a enviar
	start=time.time() # Atribui a hora atual a uma variável
	clientSocket.sendto(menssage,(serverName, 8000))# Envia uma menssage para o servidor na porta em questão

	try:
		menssage, adress=clientSocket.recvfrom(1024) #recebe uma menssage 
		tempo_decorrido = (time.time()-start) # calcula o tempo decorrido desde que começou a contar
		print (num_seq)
		print (menssage)
		print (‘viagem de ida e volta is:’ + str(tempo_decorrido) + ” segundos”) # Problema com a impressão decorrida, a menos que tenha sido alterada para uma string

	except socket.timeout: # Se o socket levar acima de 1 segundo, ele faz o seguinte, em vez do try
	print (num_seq)
	print ("Solicitação expirada")

