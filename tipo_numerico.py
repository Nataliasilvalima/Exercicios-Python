""""
Tipo numerico
// devolve valor inteiro
/ devolve valor float
** potencia
type() pergunta o tipo de variavel

Tipo float

Casas decimais com ponto e nao virgula

numeros complexos so adicionar ao numero o j

converter numeros float para inteiros perde a precisao

Tipo booleano

Algebra booleana

2 constantes= verdadeiro ou falso
True -> verdadeiro
False -> falso

"""

num = 1_000_000

print(num)

# jeito errado de float
valor = 1, 44
print(valor)
print(type(valor))

# jeito certo de float
valor2 = 1.44
print(valor2)
print(type(valor2))

# maneira de converter float para inteiro
res = int(valor2)
print(res)
print(type(res))

# Podemos usar os numeros complexos
variavel = 5j

print(float(num))

ativo = False
logado = False

print(ativo)

# operacões basicas

# Negação (not):

"""
Fazendo a negacao se o valor booleano for verdadeiro o resultado sera falso
se for falso sera verdadeiro
"""

print(not ativo)

# Ou (or)
"""
è uma operação binaria ou um ou outro deve ser verdadeiro.
"""

print(ativo or logado)
