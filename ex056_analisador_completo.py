# analisa nome, idade e sexo de um grupo de pessoas

somaIdade = 0
maisVelho = 0
mulheres = 0
nomeMaisVelho = '___'

for p in range(1, 5):
    print(f"{f' {p}ª PESSOA ':-^20}")
    nome = input('Nome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    somaIdade += idade
    if idade > maisVelho and sexo == 'M':
        maisVelho = idade
        nomeMaisVelho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1

print(f'A media de idade do grupo e de {somaIdade / 4:.1f} anos\n'
      f'O homem mais velho tem {maisVelho} anos e se chama {nomeMaisVelho}\n'
      f'Ao todo tem {mulheres} mulher(es) com menos de 20 anos')
