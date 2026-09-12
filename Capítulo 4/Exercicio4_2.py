#Exercício 4.2 
velocidade = float(input("Digite a velocidade do seu carro:"))

if velocidade > 80:
    multa = velocidade * 5
    print(f"Você foi multado(a)! O valor da multa será R${multa:5.2f}")

if velocidade <= 80:
    print("Velocidade dentro do limite.")
