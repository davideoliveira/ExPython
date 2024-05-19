n1 = float(input('Qual o valor do produto? R$'))
cdesconto = n1 - (n1 *5/100)

print(f'O produto que custava R${n1}, na promoção com desconto de 5% vai custar R${cdesconto:.2f}')