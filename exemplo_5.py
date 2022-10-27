"""
Funções - def em Python (Parte 1)
"""

print('\n' + '--' * 31 + '-\n')

def funcao():
    print('Hello World!')

funcao()

print('\n' + '--' * 31 + '-\n')


def function(msg):
    print(msg)

function('Mensagem')

print('\n' + '--' * 31 + '-\n')


def saudacao(msg='Olá', nome='usuário'):
    print(msg, nome)

saudacao()
saudacao('Pedro', 'Boa Noite')
saudacao(nome='Zezinho', msg='Hi')
saudacao('Olá', 'Robert')
saudacao('Hello', 'Cleiton')
saudacao('你好', '冠军')

print('\n' + '--' * 31 + '-\n')


def func(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    #print(msg, nome)
    return f'{msg} {nome}'

#func('Hello', 'Cleiton')

variavel = func()

print(variavel)

print('\n' + '--' * 31 + '-\n')