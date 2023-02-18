# analisa se a pessoa esta na maioridade ou menoridade

from datetime import date
anoAtual = date.today().year
contaMaiores = 0
contaMenores = 0

for p in range(1, 8):
    anoNascimento = int(input(f'Em que ano a {p}ª pessoa nasceu? '))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        contaMaiores += 1
    else:
        contaMenores += 1

print(f'Ao todo tivemos {contaMaiores} pessoas maiores de idade\n'
      f'E tambem tivemos {contaMenores} pessoas menores de idade')
