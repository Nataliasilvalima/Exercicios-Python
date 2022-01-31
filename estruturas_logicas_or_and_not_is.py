"""
Estruturas logicas: and, or, not, is

Operadores unitarios:
  not, is

Operadores binarios:
  and, or,
"""
ativo = True
logado = False

if ativo and logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa estar ativo ..por favor ativar sua conta.')

if ativo or logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa estar ativo ..por favor ativar sua conta.')

if not ativo:
    print('Bem vindo usuário!')
else:
    print('Você precisa estar ativo ..por favor ativar sua conta.')

if ativo is logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa estar ativo ..por favor ativar sua conta.')



