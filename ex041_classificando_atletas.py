# Categoria
from datetime import date
anoNascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificacao: MIRIM')
elif idade <= 14:
    print('Classificacao: INFANTIL')
elif idade <= 19:
    print('Classificacao: JUNIOR')
elif idade <= 25:
    print('Classificacao: SENIOR')
else:
    print('Classificacao: MASTER')
