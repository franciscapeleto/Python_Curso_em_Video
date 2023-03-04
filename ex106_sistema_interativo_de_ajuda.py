# programa que mostra a ajuda de uma funcao ou biblioteca escolhido pelo usuario

c = ('\33[m',       # 0 = sem cor
     '\33[0;41m',   # 1 = vermelho
     '\33[0;42m',   # 2 = verde
     '\33[0;43m',   # 3 = amarelo
     '\33[0;44m',   # 4 = azul
     '\33[0;45m',   # 5 = roxo
     '\33[7;40m',   # 6 = branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando\'{com}\'', 4)
    print(c[6], end='')
    print(help(com))


def titulo(msg, cor=0):
    print(c[cor], end='')
    print(f'-' * (len(msg) + 4))
    print(f'  {msg}')
    print(f'-' * (len(msg) + 4))
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    fB = input('Funcao ou Biblioteca > ').strip().lower()
    if fB == 'fim':
        break
    else:
        ajuda(fB)
titulo('ATE LOGO!', 1)
