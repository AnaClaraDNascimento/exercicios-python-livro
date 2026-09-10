#Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, 
# cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.


distancia = float(input("Digite a distância que você deseja percorrer em km:"))

if distancia <= 200:
    valor = (distancia * 0.5)
    print(f"O preço da passagem será R${valor:5.2f}")
else:
    valor = (distancia * 0.45)
    print(f"O preço da passagem será R${valor:5.2f}")