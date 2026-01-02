import datetime #importando biblioteca datetime
import plataform #importando biblioteca plataform
import os #importando biblioteca os

user_input = input("Enter the network IP: ") #retorna "Enter the network IP: " e e coleta o input do usuário
ip_parts = user_input.split('.') #separa as seções do ip do input do usuário
network_ip = ip_parts[0]+'.'+ip_parts[2]+'.' #junta novamente as seções do ip do usuário desejadas separadas por "."
first_host = int(input("Enter the first number: ") #define primeiro host para ping
last_host = int(input("Enter the last number: ") #define último host para ping
last_host += 1 #adiciona 1 ao último host para inclui-lo ao scan
oper = plataform.system() #verfica o sistema operacional em que o script está sendo executado e armazena na variável 'oper'
if(oper == "Windows"): #executa uma operação com base no os para adequar o ip
  ping = "ping -n 1 "
else:
  ping = "ping -c 1 "
time1 = datetime.datetime.now() #determina o tempo de execução do script com base no tempo de inicio
print("Scanning in progress.") #retorna "Scanning in progress"

for ip in range(first_host,last_host): #é definido o range do scan
  addr = network_ip + str(ip) #junta-se o ip da rede + ip do range para obter o alvo
  command = ping + addr #prepara o ping para ser ativado como 'command'
  response = os.popen(command) #salva o retorno dos pings como 'response'

  for line in list: # # retorna o 'addr(ip do alvo) + --> Live' se o alvo responder ao ping
    if(line.count("TTL")):
      print(addr, "--> Live")
      break #termina o script

#este script foi feito baseando-se no artigo da infoseccafe
