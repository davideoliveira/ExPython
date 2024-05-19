dias = int(input('Quantod dias alugados: '))
km = float(input('Quantos KMs rodados: '))
valor = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${valor}')