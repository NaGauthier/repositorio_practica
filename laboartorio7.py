#condicionales
edad = 18

if edad >= 18:
    print("Bienvenida")
else:
    print("Lo siento, debes tener al menos 18 años.")

    userReply = input("Do you need to ship a package? (Enter yes or no) ")
    
    # Solicitar al usuario que ingrese su país
pais = input("Ingresa tu país: ")

# Condicionales para verificar el país ingresado
if pais == "Chile":
    print("Buena poh")
elif pais == "Colombia":
    print("Hola parce")
else:
    print("Hola chamo")
    


