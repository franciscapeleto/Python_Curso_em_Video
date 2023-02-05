# dissecando uma variável

algo = input('Digite algo: ') # usuário deve inserir qualquer informação na variável algo
print('O tipo primitivo do que foi digitado é ', type(algo)) # imprime o tipo primitivo da variável algo
print('O que foi digitado somente tem espaços? ', algo.isspace()) # imprime se a variável algo só tem espaços
print('O que foi digitado é um número? {}'.format(algo.isnumeric())) # imprime se a variável algo é um número
print('O que foi digitado é alfabético? {}'.format(algo.isalpha())) # imprime se a variável algo é alfabético
print('O que foi digitado é alfanumérico? {}'.format(algo.isalnum())) # imprime se a variável algo é alfanumérico
print('O que foi digitado está com letras maiúsculas? {}'.format(algo.isupper())) # imprime se a variável algo \
# está com letras maiúsculas
print('O que foi digitado está com letras minúsculas? {}'.format(algo.islower())) # imprime se a variável algo \
# está com letras minúsculas
print('O que foi digitado está com letras capitalizadas? {}'.format(algo.istitle())) # imprime se a variável algo \
# está com letras capitalizadas
