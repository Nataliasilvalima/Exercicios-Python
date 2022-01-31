"""
Recebendo dados do usuario
input() é a entrada de dados e  todos os dados tem o tipo string

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Cast é a conversao de um tipo de dado para outro

"""
print("Qual seu nome")
nome = input()  # Input é a entrada

print("Qual a sua idade")
idade = input()

print("Seja bem - vindo(a) %s" % nome)  # forma antiga

print("Seja bem - vindo(a) {0}".format(nome))  # forma moderna

print(f"Seja bem - vindo(a) {nome}")  # forma atualizada

print("A %s tem %s anos" % (nome, idade))  # forma antiga

print("A {0} tem {1} anos".format(nome, idade))  # fomra moderna

print(f"A {nome} tem {idade} anos")  # forma atualizada

print(f"A {nome} nasceu em {2021 - int(idade)}")

idade = int(input('Qual a dua idade?'))

print(f"Sua idade é {idade}")
