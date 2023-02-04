# Verifica se a cidade que o usuário nasceu comeca com Santo
cidadeNatal = input('Em que cidade voce nasceu? ').strip().capitalize()
print('A cidade que voce nasceu comeca com Santo? {}'.format('Santo' in cidadeNatal))
