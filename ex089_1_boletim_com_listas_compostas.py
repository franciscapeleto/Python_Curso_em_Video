# usuario inseri nome do aluno mais duas notas
# programa mostra a media de cada aluno
# programa mostra as notas de cada aluno caso o usuario queira

ficha = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 12)
print(f'{"No.":<5}{"NOME":<10}{"MEDIA":>9}')
print('-' * 24)

for c, nomeMedia in enumerate(ficha):
    print(f'{c:<5}{nomeMedia[0]:<10}{nomeMedia[2]:>9.1f}')

posicao = 0
while posicao != 999:
    print('-' * 40)
    posicao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for c, notas in enumerate(ficha):
        if posicao == c:
            print(f'Notas de {notas[0]} sao {notas[1]}')

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')