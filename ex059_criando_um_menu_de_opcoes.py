# menu de opcoes

from time import sleep
sair = False
opcao4 = True

while sair == False:
    while opcao4 == True:
        primeiroNum = int(input('Primeiro valor: '))
        segundoNum = int(input('Segundo valor: '))
        opcao4 = False
    print('''\t[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual e a sua opcao? '))
    if opcao == 1:
        soma = primeiroNum + segundoNum
        print(f'A soma entre {primeiroNum} + {segundoNum} e igual a {soma}')
        opcao4 = False
    elif opcao == 2:
        produto = primeiroNum * segundoNum
        print(f'A multiplicacao entre {primeiroNum} x {segundoNum} e igual a {produto}')
        opcao4 = False
    elif opcao == 3:
        if primeiroNum > segundoNum:
            print(f'Entre {primeiroNum} e {segundoNum} o maior valor e {primeiroNum}')
        elif segundoNum > primeiroNum:
            print(f'Entre {primeiroNum} e {segundoNum} o maior valor e {segundoNum}')
        else:
            print(f'Entre {primeiroNum} e {segundoNum} nao tem valor maior, eles sao iguais')
        opcao4 = False
    elif opcao == 4:
        opcao4 = True
        print('Informe os numero novamente:')
    elif opcao == 5:
        sair = True
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
