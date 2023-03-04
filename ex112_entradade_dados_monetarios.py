# mostra diferente valores com base em um valor escolhido pelo usuario

from ex112.utilidades import moeda
from ex112.utilidades import dado

p = dado.leiaDinheiro('Digite o preco: R$ ')
moeda.resumo(p, 20, 12)