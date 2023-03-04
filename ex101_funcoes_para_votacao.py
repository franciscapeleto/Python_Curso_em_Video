# mostra o maior valor de numeros aleatorios

def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade < 16:
        return f'Com {idade} anos: NAO VOTA.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


print('-' * 40)
anoNasc = int(input('Em que ano voce nasceu? '))
print(voto(anoNasc))
