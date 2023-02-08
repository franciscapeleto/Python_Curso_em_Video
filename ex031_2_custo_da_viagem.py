# Calcula o preco da passagem
distancia = float(input('Qual e a distancia da sua viagem? '))
print(f'Voce esta prestes a comecar uma viagem de {distancia}Km')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preco da sua passagem sera de R${preco:,.2f}')
