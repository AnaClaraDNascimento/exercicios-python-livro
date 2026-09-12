#Exercício 4.4

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
