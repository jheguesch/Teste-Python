print('+------------------------------------------------+')
print('|                                                |')
print('|                   Bem-Vindo                    |')
print('|                      ao                        |')
print('|                 Menu de Opções                 |')
print('|                                                |')
print('+------------------------------------------------+')
print('|                                                |')
print('|         Escolha uma das opções abaixo          |')
print('|             para dar continuidade              |')
print('|                                                |')
print('|              1 -  Criptografar                 |')
print('|              2 - Descriptografar               |')
print('|              3 -     Sair                      |')
print('|                                                |')
print('|                                                |')
print('| Sugestão de frase e chave:                     |')
print('|                                                |')
print('| Frase para criptografar: o lobo ama o bolo     |')
print('| Chave para usar: corsa                         |')
print('|                                                |')
print('+------------------------------------------------+')

rotacao = 13
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


while rotacao != 0:
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        print('Opção escolhida: 1 - Criptografar')
    elif opcao == 2:
        print('Opção escolhida: 2 - Descriptografar')
    elif opcao == 3:
        print('Opção escolhida: 3 - Sair')
        print('\nObrigado pela atenção! Até a próxima :)')
        break
    else:
        print('Alguma coisa deu errada! Digite apenas as opção fornecidas!')
        break

    texto = ''.join(str(input('Digite a frase: ')).upper().split())
    chave = str(input('Digite uma Chave: ')).upper()
    TextoFinal = ''
    ChaveFinal = ''

    if(len(chave) > len(texto)):
        print('A Chave é maior que a frase!\n')

    else:
        i = int(0)
        while (len(ChaveFinal) < len(texto)):
            ChaveFinal += chave[i]
            i += 1
            if(i == len(chave)):
                i = 0

        for i in range(len(texto)):
            if(texto[i]) != ' ':
                posicao_frase = int(alfabeto.index(texto[i]))
                posicao_chave = int(alfabeto.index(ChaveFinal[i]))
                if(opcao == 1):
                    TextoFinal += str(alfabeto[(posicao_frase +
                                                posicao_chave) % len(alfabeto)])
                else:
                    TextoFinal += str(alfabeto[(posicao_frase -
                                                posicao_chave) % len(alfabeto)])
            else:
                TextoFinal += i

        print(f'\nFrase Final: {TextoFinal}')
        print(f'Chave usada: {chave}')
        continuar = str(input('\nDeseja continuar? (s/n): '))
        if continuar == 's':
            print('Aperte enter para continuar!')
            input()
        else:
            print('\nObrigado pela atenção! Até a próxima :)')
            break
