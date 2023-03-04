# mostra o maior valor de numeros aleatorios

def notas(*notas, sit=False):
    '''
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param notas: uma ou notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma
    '''
    print('-' * 40)
    r = {}
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['media'] = sum(notas)/len(notas)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5.5, 9.5, 0, 6.5, 0, sit=True)
print(resp)
