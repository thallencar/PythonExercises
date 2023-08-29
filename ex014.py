#Exercício 013: Conversor de temperaturas. Escreva um programa que converta uma temperatura digitada em C° para F°, K°, R° e Raº.
temp_C = float(input("Digite a temperatura em C°: "))

temp_F = temp_C * 1.8 + 32
temp_K = temp_C + 273


print(f""" 
      -----------------------------------------
      ======= CONVERSOR DE TEMPERATURAS =======
      {temp_C} C° em F°, equivale à: {temp_F:.1f}
      {temp_C} C° em K°, equivale à: {temp_K:.1f}
      ================== FIM ==================
      -----------------------------------------
    """)
