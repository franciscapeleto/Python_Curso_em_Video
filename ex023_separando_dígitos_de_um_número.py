# Separa unidade, dezena, centena e milhar de um numero de 0 a 9999
numero = int(input('Digite um numero de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('\33[1;7;31munidade{}{:->3}{}'.format('\33[0;31m', unidade, '\33[m'))
print('\33[1;7;32mdezena{}{:->4}{}'.format('\33[0;32m', dezena, '\33[m'))
print('\33[1;7;33mcentena{}{:->3}{}'.format('\33[0;33m', centena, '\33[m'))
print('\33[1;7;34mmilhar{}{:->4}{}'.format('\33[0;34m', milhar, '\33[m'))
