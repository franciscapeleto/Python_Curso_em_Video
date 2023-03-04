# usuario cadastra nome e peso de uma pessoa quantas vezes desejar
# o programa analise quantas pessoas foram cadastradas e quais pessoas tem o maior e o menor peso

nomePeso = []
dados = []
dadoMaior = []
dadoMenor = []
maior = menor = 0

while True:
    nomePeso.append(input('Nome: '))
    nomePeso.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = nomePeso[1]
    else:
        if maior < nomePeso[1]:
            maior = nomePeso[1]
        if menor > nomePeso[1]:
            menor = nomePeso[1]
    dados.append(nomePeso[:])
    nomePeso.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Ao todo, voce cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de', end=' ')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
