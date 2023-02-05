# Mostrar o primeiro e ultimo nome do usuário

nomeCompleto = input('Digite seu nome completo: ').strip().title()
nomeSeparado = nomeCompleto.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome e "{}"'.format(nomeSeparado[0]))
print('Seu ultimo nome e "{}"'.format(nomeSeparado[-1]))
