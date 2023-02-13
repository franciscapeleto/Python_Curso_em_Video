# Alistamento Militar
from datetime import date
ano = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {anoAtual}.')

if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    anoAlistamento = ano + 18
    if saldo == 1:
        print(f'Ainda falta {saldo} ano para o alistamento.\n'
              f'Seu alistamento sera em {ano + 18}.')
    else:
        print(f'Ainda faltam {saldo} anos para o alistamento.\n'
              f'Seu alistamento sera em {ano + 18}.')
else:
    saldo = idade - 18
    anoAlistamento = ano + 18
    if saldo == 1:
        print(f'Voce ja deveria ter se alistado ha {saldo} ano.\n'
              f'Seu alistamento foi em {anoAlistamento}.')
    else:
        print(f'Voce ja deveria ter se alistado ha {saldo} anos.\n'
              f'Seu alistamento foi em {anoAlistamento}.')
