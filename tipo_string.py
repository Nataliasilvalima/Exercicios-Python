"""
Tipo String

Em python um dado é considerado uma string sempre que:
 estiver em aspas simples ou duplas
 upper() = maiuscula
 lower() = minuscula
 split() = cria uma lista separada por palavras
"""
nome = "natAliA"
print(nome.upper())

print(nome.title())

print(nome.lower())

nome2 = "Geek university"

print(nome2.split())

print(nome2[0:4])  # imprimi somente o numero de vetores selecionados.

print(nome2.title()[5:15])  # imprimi somente o numero de vetores selecionados.

print(nome2[:: -1])  # imprimi todas as letras de forma invertida.

print(nome2[::])  # imprime as palavras de forma do vetor de primeira ate a ultima letra.

print(nome2.replace('e', 'i'))





