#Exercício 06: Dobro, Triplo, Raiz. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = int(input("Digite um número\n > "))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print(f"O dobro de {num} vale {dobro}.")
print(f"O triplo de {num} vale {triplo}.")
print(f"A raiz de {num} vale {raiz}.")
