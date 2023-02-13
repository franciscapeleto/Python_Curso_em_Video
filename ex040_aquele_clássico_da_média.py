# Media de notas

nota1 = float(input('Primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a media do aluno e {media:.2f}')

if media >= 7:
    print('O aluno esta APROVADO')
elif 5 <= media < 7:
    print('O aluno esta de RECUPERACAO')
else:
    print('O aluno esta REPROVADO')
