"""
Escopo de variaveis

Dois casos de escopo:

1- Variaveis locais = declara em funçoes
2- Variaveis globais = declarada no programa
"""

"""
If Else e elif
"""
print("Qua a sua idade?")

idade = input()

if int(idade) > 18:
    print("Maior de idade, sua idade é %s" % idade)
elif int(idade) == 18:
    print("Parabens você tem 18 anos e passou no teste")
elif int(idade) == 20:
    print("Parabens você tem 20 anos porem nao passou no teste")
else:
    print("Menor de idade a esperada não esta autorizado. Sua idade %s" % idade)

