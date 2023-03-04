# analise de dados do grupo

contadorMaior = contadorHomem = contadorMulherMenor = 0

while True:
    print('-' * 40)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print('-' * 40)
    sexo = continuar = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    print('-' * 40)
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if idade >= 18:
        contadorMaior += 1
    if sexo == 'M':
        contadorHomem += 1
    if idade < 20 and sexo == 'F':
        contadorMulherMenor += 1
    if continuar == 'N':
        break

print('-'*40)
print(f"Total de pessoa(s) com mais de 18 anos: {contadorMaior}")
print(f'Ao todo temos {contadorHomem} homem(ns) cadastrado(s)')
print(f'E temos {contadorMulherMenor} mulher(es) com menos de 20 anos')
