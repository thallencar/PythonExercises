#Exercício 011: Pintando paredes. Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e quantidade de latas de tinta necessárias para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input("Digite a largura da parede:\n > "))
h = float(input("Digite a altura da parede:\n > "))

area = l * h 
lata_tinta = area / 2

print(f"""Sua parede tem a dimensão de {l}x{h} e sua área é de {area}m². 
Para pintar essa parede, você precisará de {lata_tinta}l de tinta.""")