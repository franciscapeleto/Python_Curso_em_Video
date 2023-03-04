# mostra o maior valor de numeros aleatorios

def notas(*notas, sit=False):
    '''
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param notas: uma ou notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma
    '''
    print('-' * 40)
    total = len(notas)
    maior = menor = 0
    for c, n in enumerate(notas):
        if c == 0:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    media = sum(notas) / total
    if media >= 7:
        situacao = 'BOA'
    elif 5 <= media < 7:
        situacao = 'RAZOAVEL'
    else:
        situacao = 'RUIM'
    if sit:
        dicionarioNotas = {'total': total, 'maior': maior, 'menor': menor, 'media': media, 'situacao': situacao}
    else:
        dicionarioNotas = {'total': total, 'maior': maior, 'menor': menor, 'media': media}
    return dicionarioNotas


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
