#Exercício 013: Reajuste salarial. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento (deixei opcional)

sal = float(input("Digite o seu atual salário:\n > "))
porc = float(input("Digite a porcentagem a ser reajustada:\n > "))

reajuste = sal + (sal * porc/100) 

print(f"Um funcionário que ganhava R${sal}, com {porc}% de aumento, passa a ganhar R${reajuste:.2f}.")
