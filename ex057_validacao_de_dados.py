# valida somente M e F

sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]

while sexo not in 'MF':
    sexo = input('Dados invalidos. Por favor, informe seu sexo: ').strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso')
