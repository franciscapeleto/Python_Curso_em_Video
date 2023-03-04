# mostra diferente valores com base em um valor escolhido pelo usuario

from ex110 import moeda

p = float(input('Digite o preco: R$ '))
m = int(input('Qual moeda voce deseja? [1=Real / 2=Dolar] '))
a = int(input('Quantos porcentos de aumento? '))
r = int(input('Quantos porcentos de reducao? '))
moeda.resumo(p, a, r, m)