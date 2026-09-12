#Exercicio 4.10
kwh = int(input("Digite a quantidade de kWh consumida:"))
tipo = str(input("Digite o tipo de instalação(R ou I ou C):")).strip().upper()
if tipo == "R":
  if kwh <= 500:
    total = kwh * 0.4
    print(f"Você pagará R${total:6.2f}")
  elif kwh > 500:
    total = kwh * 0.65
    print(f"Você pagará R${total:6.2f}")
elif tipo == "C":
  if kwh <= 1000:
    total = kwh * 0.55
    print(f"Você pagará R${total:6.2f}")
  elif kwh > 1000:
    total = kwh * 0.6
    print(f"Você pagará R${total:6.2f}")
elif tipo == "I":
  if kwh <= 5000:
    total = kwh * 0.55
    print(f"Você pagará R${total:6.2f}")
  elif kwh > 5000:
    total = kwh * 0.6
    print(f"Você pagará R${total:6.2f}")
else:
  print("Ocorreu um erro. Tente novamente mais tarde!")


