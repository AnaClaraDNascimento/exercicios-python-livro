#Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Digite o valor do seu salário:"))

if salario > 1250:
    aumento = (salario * 0.1)
    total = (salario + aumento)
    print(f"O aumento ficou R${aumento:5.2f}")
    print(f"O seu salário ficou R${total:5.2f}")


if salario <= 1250:
    aumento = (salario * 0.15)
    total = (salario + aumento)
    print(f"O aumento ficou R${aumento:5.2f}")
    print(f"O seu salário ficou R${total:5.2f}")
