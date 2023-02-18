# analisa o maior peso e o menor peso entre 5 pesos digitados

pesoMaior = 0
pesoMenor = 0

for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        pesoMenor = peso
        pesoMaior = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        elif peso < pesoMenor:
            pesoMenor = peso

print(f'O maior peso lido foi de {pesoMaior:.1f}Kg\n'
      f'O menor peso lido foi de {pesoMenor:.1f}Kg')
