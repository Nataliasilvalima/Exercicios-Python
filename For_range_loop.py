"""
Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis
"""

nome = 'Geek Univerisity'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for letra in nome:  # itterando sobre uma string
    print(letra)

for numero in lista:  # iterando sobre uma lista
    print(numero)

for numero in range(1, 10):  # Não inclui o valor final. valor final menos 1
    print(numero)

for i, v in enumerate(nome):  # imprimi cada letra em uma linha e pula para a inha posterior
    print(nome[i])

for i, v in enumerate(nome):  # ele conta a quantidade de letras e imprimi cada palavra  em uma linha
    print(nome)

for valor in enumerate(nome):  # imprimi o valor do indice e a letra na posição.
    print(valor)

for valor in enumerate(nome):  # imprimi o valor do indice
    print(valor[0])

qnt = int(input('Quantas vezes esse looping tem que rodar?'))

for n in range(1, qnt+1):
    print(f'Imprimindo {n}')

for letra in nome:     # ele imprimime com espaço sem pular linha
    print(letra, end='')



