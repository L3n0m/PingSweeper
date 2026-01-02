import datetime  # importando biblioteca datetime para medir o tempo de execução
import platform  # importando biblioteca platform para identificar o sistema operacional
import os        # importando biblioteca os para executar comandos no sistema

user_input = input("Enter the network IP (ex: 192.168.0.1): ")  # solicita o IP base da rede ao usuário
ip_parts = user_input.split('.')  # separa o IP em partes usando o ponto como delimitador

network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'  
# reconstrói o IP da rede mantendo os três primeiros octetos (ex: 192.168.0.)

first_host = int(input("Enter the first host number: "))  # define o primeiro host a ser testado
last_host = int(input("Enter the last host number: "))    # define o último host a ser testado
last_host += 1  # adiciona 1 para incluir o último host no range do scan

oper = platform.system()  # identifica o sistema operacional em que o script está sendo executado

if oper == "Windows":  # define o comando ping de acordo com o sistema operacional
    ping = "ping -n 1 "  # parâmetro -n é usado no Windows
else:
    ping = "ping -c 1 "  # parâmetro -c é usado em sistemas Unix/Linux

time1 = datetime.datetime.now()  # registra o horário de início do scan
print("Scanning in progress...\n")  # informa ao usuário que o scan foi iniciado

for ip in range(first_host, last_host):  # percorre o range de hosts definido pelo usuário
    addr = network_ip + str(ip)  # monta o endereço IP completo do host atual
    command = ping + addr        # prepara o comando de ping a ser executado
    response = os.popen(command) # executa o comando e armazena a resposta

    for line in response:  # percorre cada linha da resposta do ping
        if "TTL" in line:  # verifica se a resposta contém TTL (indica host ativo)
            print(addr, "--> Live")  # informa que o host está ativo
            break  # sai do loop de leitura da resposta para este host

time2 = datetime.datetime.now()  # registra o horário de término do scan
print("\nScan completed in:", time2 - time1)  # exibe o tempo total de execução do scan

# -------------------------------------------------------------------------
# Este projeto foi desenvolvido como exercício educacional e de aprendizado.
# A base conceitual do funcionamento do ping sweep foi estudada a partir de
# artigos do blog InfoSec Café, utilizados como referência teórica e didática.
# A implementação do código, comentários e organização são autorais.
#                                                                  Ass. L3n0m :p
# -------------------------------------------------------------------------
