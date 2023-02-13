# Conversor de Bases Numericas
numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = input('Sua opcao: ')

if opcao == '1':
      print(f'{numero} convertido para BINARIO e igual a {bin(numero)[2:]}')
elif opcao == '2':
      print(f'{numero} convertido para OCTAL e igual a {oct(numero)[2:]}')
elif opcao == '3':
      print(f'{numero} convertido para HEXADECIMAL e igual a {hex(numero)[2:]}')
else:
      print('Opcao invalida. Tente novamente.')
