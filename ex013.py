salario = float(input('Qual o sálerio do funcionário? R$'))
caumento = salario + (salario * 15/100)

print(f'Um funcionário queganhava {salario}, com 15% de aumento, passa a receber R${caumento:.2f}')