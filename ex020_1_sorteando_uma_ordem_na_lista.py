# sorteia a ordem que os alunos irão apresentar o trabalho

from random import shuffle
alunos = ['Roberto', 'Paulo', 'Maria', 'Joaquina']
shuffle(alunos)
n = 1

for a in alunos:
    print('O {}o aluno que irá apresentar o trabalho será "{}".'.format(n, a))
    n += 1
