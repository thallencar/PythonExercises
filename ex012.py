#Exercício 012: Calculando descontos. Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
preco = float(input("Digite o preço do produto:\n > "))

v_final = preco - (preco * 5/100) 





print(f"O produto que custava R${preco}, na promoção com 5% de desconto, vai custar R${v_final}.")