#Exercício 15: Aluguel de carros. Escreva um programa que pergunte a quantidade de km's percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a ser pago, sabendo que o carro custo R$60 por dia e R$0,15 por km's rodados.
dias = int(input("Há quantos dias o carro está alugado?\n > "))
km = int(input("Quantos Km's rodados?\n > "))

valor_aluguel = (km*0.15) + (dias*60)

print(f"O valor a ser pago pelo aluguel é de R${valor_aluguel:.2f}.")