# Ping Sweeper em Python

## Descrição

Este projeto consiste em um **ping sweeper simples**, desenvolvido em Python, com o objetivo de identificar hosts ativos em uma rede local.  
O script realiza o envio de pacotes ICMP (ping) para um intervalo de endereços IP definido pelo usuário e identifica quais hosts respondem.

Este projeto foi criado **exclusivamente como exercício educacional**, visando o aprendizado e aplicação de cnceitos.

---

## Funcionamento Geral

1. O usuário informa um endereço IP base da rede (ex: `192.168.0.1`)
2. O script extrai os três primeiros octetos para definir a rede
3. O usuário define o intervalo de hosts a serem testados
4. O script executa o comando `ping` para cada host do intervalo
5. Caso o host responda ao ping, ele é exibido como **ativo**
6. Ao final, o tempo total de execução é apresentado

---

## Requisitos

- Python 3.x

Nenhuma biblioteca externa é necessária.
nenhum sistema operácional específico necessário.

---

## Execução

'python ping_sweeper.py'

---

## Créditos

Script formulado com base no artigo sobre ping Sweepers da infosec cafe.
