# usuario inseri nome do aluno mais duas notas
# programa mostra a media de cada aluno
# programa mostra as notas de cada aluno caso o usuario queira

listaTemp = []
listaMedia = []

while True:
    listaTemp.append(input('Nome: '))
    listaTemp.append(float(input('Nota 1: ')))
    listaTemp.append(float(input('Nota 2: ')))
    listaMedia.append(listaTemp[:])
    listaTemp.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 12)
print(f'{"No.":<5}{"NOME":<10}{"MEDIA":>9}')
print('-' * 24)

for c, nomeMedia in enumerate(listaMedia):
    media = (nomeMedia[1] + nomeMedia[2]) / 2
    print(f'{c:<5}{nomeMedia[0]:<10}{media:>9}')

posicao = 0
while posicao != 999:
    print('-' * 40)
    posicao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for c, notas in enumerate(listaMedia):
        if posicao == c:
            print(f'Notas de {notas[0]} sao {notas[1:]}')

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')