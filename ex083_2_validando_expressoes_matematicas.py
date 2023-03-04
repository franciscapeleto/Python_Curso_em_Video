# usuario digita numeros ate ele decidir nao continuar e os numeros sao adicionados
# em uma lista ordem decrescente, mostra o total de numeros digitados e se o numero 5 esta na lista

contadoAbrir = contadorFechar = 0
expressao = input('Digite a expressao ')

for e in expressao:
    if e == '(':
        contadoAbrir += 1
    elif e == ')':
        contadorFechar += 1

if contadoAbrir == contadorFechar:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta errada!')