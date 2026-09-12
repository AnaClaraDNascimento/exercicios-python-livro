#Exercício 4.3

a = int(input("Digite primeiro valor:"))
b = int(input("Digite segundo valor:"))
c = int(input("Digite terceiro valor:"))

if a > b and c:
    print(f"O primeiro valor {a} é o maior!")

if b > a and c:
    print(f"O segundo valor {b} é o maior!")

    
if c > a and b:
    print(f"O terceiro valor {c} é o maior!")
    

if a < b and a < c:
    print(f"O primeiro valor {a} é o menor!")

if b < a and b < c:
    print(f"O segundo valor {b} é o menor!")

    
if c < a and c < b:
    print(f"O terceiro valor {c} é o menor!")
