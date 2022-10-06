#        2) Dado a sequencia de Fibonacci, onde se inicia por 0 e 1 e o proximo valor sempre
#        sera a soma dos 2 valores anteriores(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
#        escreva um programa na linguagem que desejar onde, informado um numero, ele calcule
#        a sequencia de Fibonacci e retorne uma mensagem avisando se o numero informado
#        pertence ou nao a sequencia.
#
#        IMPORTANTE:
#        Esse numero pode ser informado atraves de qualquer entrada de sua preferencia ou pode
#        ser previamente definido no codigo;

x = 0
a = 0
b = 1

print('')
print('-=' * 30 + '-')
print('')

valor = int(input("Digite um numero: "))
print("\nSérie de Fibonacci:\n")

print('-> ', a)
print('-> ', b)

while x < valor:

    aux = a + b
    a = b
    b = aux

    print('-> ', aux)
    x += 1

print('')
print('-=' * 30 + '-')
print('')

input()
