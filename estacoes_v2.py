# Estações do Ano
# Apresentação
print('\n\t\t\t  --  Estações do Ano - Simples   --')
# Entradas
mes = int(input('Informe o mês do ano (1 a 12): '))
dia = int(input('Informe o dia: '))

# Condicional e saída
if (mes == 3 and dia < 20) or (mes == 12 and dia >= 22) or (mes == 1 or mes == 2):
    print(f'Em {dia} de {mes} a estação é Verão!')
elif (mes == 6 and dia < 21) or (mes == 3 and dia >= 20) or (mes == 4 or mes == 5):
    print(f'Em {dia} de {mes} a estação é Outono!')
elif (mes == 9 and dia < 23) or mes == 6 and dia >= 21 or (mes == 7 or mes == 8):
    print(f'Em {dia} de {mes} a estação é Inverno!')
elif (mes == 12 and dia < 22) or (mes == 9 and dia >= 23) or (mes == 10 or mes == 11):
    print(f'Em {dia} de {mes} a estação é Primavera!')


