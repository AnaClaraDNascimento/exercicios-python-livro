#Exercicio 4.9
house = float(input("Digite o valor da casa:"))
salary = float(input("Digite o salário:"))
years = int(input("Digite quantos anos a pagar:"))
mouths = years * 12
installment = house / mouths
percentage = salary * 0.3

if installment <= percentage:
  print(f"Seu empréstimo foi aprovado! Valor: R${installment:6.2f}")
elif installment > percentage:
  print("Seu empréstimo foi negado!")
else:
  print("Ocorreu algum erro. Por favor, tente novamente mais tarde!")

