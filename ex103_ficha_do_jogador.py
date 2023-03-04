# mostra o maior valor de numeros aleatorios

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols.isalpha():
        gols = '0'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 40)
nomeJogador = input('Nome do Jogador: ').strip()
golsJogador = input('Numero de Gols: ').strip()
ficha(nomeJogador, golsJogador)
