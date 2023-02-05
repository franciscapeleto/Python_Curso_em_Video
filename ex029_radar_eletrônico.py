# Velocidade do carro com cobranca de multa

velocidade = float(input('Qual e a velocidade atual do carro? '))

if velocidade > 80:
    print('\33[1;31mMULTADO! Voce excdedeu o limite permitido que e de de 80Km/h')
    print('\33[0;31mVoce deve pagar uma multa de \33[1;33mR${:,.2f}!'.format((velocidade - 80)*7))
print('\33[0;4;33mTenha um bom dia! Dirija com seguranca!')
