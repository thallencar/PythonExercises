#Exercício 010: Conversor de moedas. Cire um programa que leia quanto dinheiro a pessoa quer converter e exibir o valor convertido.
real = float(input("Qual o valor em R$ a ser convertido?\n > "))

dolar = real / 4.87
euro = real / 5.28
libra = real / 6.14
yen = real / 0.0333
peso = real / 0.014

print(f"""
    -------------------------------
    CONVERSOR REAL - MOEDA
    ===============================
    R${real} BRL = ${dolar:.2f} USD 
    R${real} BRL = €{euro:.2f} EUR
    R${real} BRL = £{libra:.2f} GBP
    R${real} BRL = ¥{yen:.2f} JPY
    R${real} BRL = ${peso:.2f} ARS
    ===============================
    -------------------------------
    """)

#Estatísticas baseadas em 29/08/2023
