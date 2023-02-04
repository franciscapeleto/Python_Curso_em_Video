# Mostrar o nome completo do usuário em maiusculas, minusculas, quantidade de letras total e no primeiro nome

nomeCompleto = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em letras Maiusculas e: ' + nomeCompleto.upper())
print('Seu nome em letras Minusculas e: ' + nomeCompleto.lower())
nomeCompletoSplit = nomeCompleto.split()
print('A quantidade total de letras no seu Nome Completo e de "{}" letras.'.format(len(''.join(nomeCompletoSplit))))
print('A quantidade total de letras no seu Primeiro Nome e de "{}" letras.'.format(len(nomeCompletoSplit[0])))
