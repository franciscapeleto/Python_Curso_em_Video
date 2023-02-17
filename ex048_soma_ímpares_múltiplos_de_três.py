# Contagem regressiva

contagem = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        contagem += 1

print(f'A soma de todos os {contagem} valores solicitados e {soma}')
