# usuario cadastra nome e media de um aluno
# programa analisa se o aluno foi aprovado, em recuperacao ou reprovado

cadastro = {}
cadastro['nome'] = input('Nome: ')
cadastro['media'] = float(input(f'Media de {cadastro["nome"]}: '))

if cadastro['media'] >= 7:
    cadastro['situacao'] = 'Aprovado'
elif 5 <= cadastro['media'] < 7:
    cadastro['situacao'] = 'Recuperacao'
else:
    cadastro['situacao'] = 'Reprovado'

print('-=' * 20)

for k, v in cadastro.items():
    print(f' - {k} e igual a {v}')
