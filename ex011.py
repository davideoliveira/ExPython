num1 = float(input('Digite a largura da parede: '))
num2 = float(input('Digite a altura da parede: '))
area = num1 * num2
tinta = area / 2

print(f'Sua parede tem a dimensão de {num1}X{num2} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')