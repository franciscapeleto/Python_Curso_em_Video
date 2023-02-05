# Mostrar o primeiro e ultimo nome do usuário

nomeCompleto = input('Digite seu nome completo: ').strip().title()
primeiroEspaco = nomeCompleto.find(' ')
ultimoEspaco = nomeCompleto.rfind(' ')
print('Muito prazer em te conhecer!')
print('Seu primeiro nome e "{}"'.format(nomeCompleto[:primeiroEspaco]))
print('Seu ultimo nome e "{}"'.format(nomeCompleto[ultimoEspaco+1:]))
