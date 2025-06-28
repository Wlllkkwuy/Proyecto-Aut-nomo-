from random import choice           #Esta librería sirve para que la computadora pueda elejir una de las opciones que esán en mi variable
from datetime import datetime       #esta librería sirve para los guardados 





# Función para guardar la partida en un archivo
def guardar_partida(resultado, usuario, ia):
    # Obtenemos la fecha y hora actuales para el registro
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("partidas_guardadas.txt", "a") as archivo:
        archivo.write(f"Fecha y Hora: {fecha_hora_actual} | Usuario: {usuario} | IA: {ia} | Resultado: {resultado}\n")






# movimientos del juego
mov = ("piedra", "papel", "tijera")


#Bienvenida
print("                                                                  Hola! Bienvenido al Juego de 🪨 📝  ✂️")





# Inicio de Sesión, por ahora solo es una contraseña
pswd_real = "clase"
pswd_user = ""

while pswd_user != pswd_real:
    pswd_user = input("                                   Porfavor Coloca la Contraseña: ")
    if pswd_user != pswd_real:
        print("Contraseña incorrecta.❌")

print("Contraseña correcta. ✅")





# Bucle principal del juego
jugar_de_nuevo = "s" # Inicializamos para que el juego comience
while jugar_de_nuevo.lower() == "s": # El juego se repite mientras el usuario quiera
    Usuario = ""
    while Usuario not in mov:
        Usuario = input("Introduce un movimiento (piedra 🪨         papel 📝         tijera ✂️  : ").lower()

    ia = choice(mov)

    print(f"🙍Usuario: {Usuario}")
    print(f"💻IA: {ia}")




    # Resultados
    resultado = ""
    if ia == Usuario:
        resultado = "Empate" 
    elif (ia == "tijera" and Usuario == "piedra") or \
         (ia == "papel" and Usuario == "tijera") or \
         (ia == "piedra" and Usuario == "papel"):
        resultado = "Ganaste"
    else:
        resultado = "Perdiste"

    print(f"El resultado es: {resultado}")



    # Preguntar si desea guardar la partida
    guardar = input("¿Quieres guardar esta partida? (s/n): ").strip().lower()
    if guardar == "s":
        guardar_partida(resultado, Usuario, ia)
        print("Partida guardada en 'partidas_guardadas.txt'")
    else:
        print("No se guardó la partida.")



    # Preguntar si quiere jugar de nuevo
    print("-" * 70) 
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
    print("-" * 70) 
    

print("Gracias por jugar. ¡Hasta la próxima! 👋")
print("                                   👾Hecho por Kenneth Jair Carreño 👾")


