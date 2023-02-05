# Verifica se o numero que o usuario escolher e PAR ou IMPAR
estilo = {'padrao':'\33[0m',
          'negrito':'\33[1m',
          'sublinhado': '\33[4m'}
texto = {'branco':'\33[30m',
         'vermelho':'\33[31m',
         'verde': '\33[32m',
         'amarelo':'\33[33m',
         'azul':'\33[34m',
         'roxo':'\33[35m',
         'cinza':'\33[37m'}
numero = int(input(f'{texto["roxo"]}Me diga um numero qualquer: '))

if numero % 2 == 0:
    print(f'{texto["cinza"]}O numero {texto["azul"]}{numero} {texto["cinza"]}e {texto["azul"]}PAR')
else:
    print(f'{texto["cinza"]}O numero {texto["azul"]}{numero} {texto["cinza"]}e {texto["azul"]}IMPAR')
