# usuario cadastra nome, sexo e idade

cadastro = {}
todosCadastros = []
somaIdades = media = 0
while True:
    cadastro['Nome'] = input('Nome: ')
    while True:
        cadastro['Sexo'] = input('Sexo: [M/F] ').strip().upper()
        if cadastro['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    cadastro['Idade'] = int(input('Idade: '))
    somaIdades += cadastro['Idade']
    todosCadastros.append(cadastro.copy())
    cadastro.clear()
    while True:
        sair = input('Quer continuar? [S/N] ').strip().upper()
        if sair in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if sair == 'N':
        break
print('-=' * 40)
print(f'A) Ao todo temos {len(todosCadastros)} pessoas cadastradas.')
media = somaIdades / len(todosCadastros)
print(f"B) A media de idade e de {media:.2f} anos.")
print(f"C) As mulheres cadastradas foram ", end='')
for c in todosCadastros:
    if c['Sexo'] == 'F':
        print(c['Nome'], end=' ')
print(f"\nD) Lista das pessoas que estao acima da media:")
for c in todosCadastros:
    if c['Idade'] > media:
        print('   ', end='')
        for k, v in c.items():
            print(f"{k} = {v};", end=' ')
        print()

print('\n<< ENCERRADO >>')
