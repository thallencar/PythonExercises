#Exercício 07: Conversor de medidas. Escreva um programa que leia um valor em metros, converta e exiba em km, hm, dam, dm, cm e mm.
m = float(input("Distância em metros:\n > "))
#Conversor
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f"""A medida de {m} m, corresponde à:
    {km} Km;
    {hm} hm;    
    {dam} dam;
    {dm} dm;
    {cm} cm; 
    {mm} mm.
      """)
