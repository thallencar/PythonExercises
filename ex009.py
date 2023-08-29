#Exercício 09: Tabuada. Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
num = int(input("Digite um número:\n > "))
#tab = num * 1, num * 2, num * 3, num * 4, num * 5, num * 6, num * 7, num * 8, num * 9, num * 10
#print(f"Tabuada de {num}: {tab}")
print(f"""
    ========================
    {num} * 1 = {num * 1}
    {num} * 2 = {num * 2}
    {num} * 3 = {num * 3}
    {num} * 4 = {num * 4}
    {num} * 5 = {num * 5}
    {num} * 6 = {num * 6}
    {num} * 7 = {num * 7}
    {num} * 8 = {num * 8}
    {num} * 9 = {num * 9}
    {num} * 10 = {num * 10}
    ========================
    """)
