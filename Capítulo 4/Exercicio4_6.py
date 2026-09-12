#Exercício 4.6 
distancia = float(input("Digite a distância que você deseja percorrer em km:"))

if distancia <= 200:
    valor = (distancia * 0.5)
    print(f"O preço da passagem será R${valor:5.2f}")
else:
    valor = (distancia * 0.45)
    print(f"O preço da passagem será R${valor:5.2f}")
