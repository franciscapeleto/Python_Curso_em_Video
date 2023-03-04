# usuario cadastra um trabalhador

from datetime import datetime

cadastro = {}
cadastro['Nome'] = input('Nome: ')
cadastro['Idade'] = datetime.today().year - (int(input(f'Ano de Nascimento: ')))
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 nao tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Contratacao'] = int(input('Ano de Contratacao: '))
    cadastro['Salario'] = float(input('Salario: '))
    cadastro['Aposentadoria'] = 35 + cadastro['Contratacao'] + cadastro['Idade'] - datetime.today().year

print('-=' * 20)

for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')
