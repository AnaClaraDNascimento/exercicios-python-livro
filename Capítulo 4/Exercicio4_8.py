#Exercicio 4.8
num_1 = int(input("Digite um número:"))
num_2 = int(input("Digite outro número:"))
operation = str(input("Digite o nome de uma operação:"))

if operation == "soma":
    total = num_1 + num_2
    print(f"O resultado: {num_1} + {num_2} = {total}")
elif operation == "subtração":
    total = num_1 - num_2
    print(f"O resultado: {num_1} - {num_2} = {total}")
elif operation == "multiplicação":
    total = num_1 * num_2
    print(f"O resultado: {num_1} x {num_2} = {total}")
elif operation == "divisão":
    total = num_1 / num_2
    print(f"O resultado: {num_1} : {num_2} = {total}")
else:
    print("Esta operação é inválida. Tente novamente!")
