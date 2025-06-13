# Simblolos:    []  {}  \n 
#Piedra, Papel o tijeras


from random import choice



mov = ["piedra", "papel", "tijera"]       

Usuario =  -1  



while Usuario not in mov:
    Usuario = input("Introduce un movimiento:   ")

ia = choice(mov)

print(f"Upasuario: {Usuario}")
print(f"IA: {ia}")

if ia == Usuario:
    print("El resultado es empate :D ")



if ia == "tijera" and Usuario == "piedra":
    print ("Has ganado :D")

if ia == "tijera" and Usuario == "papel":
    print ("Has perdido!")



if ia == "papel" and Usuario == "tijera":
    print ("Has ganado!")

if ia == "papel" and Usuario == "piedra":
    print ("Has perdido!")


if ia == "piedra" and Usuario == "papel":
    print ("Has ganado!")

if ia == "piedra" and Usuario == "tijera":
    print ("Has perdido!")

print("hecho por Kenneth Jair Carreño :D")
