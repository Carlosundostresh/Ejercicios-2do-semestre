small = 2
regular = 5
big = 6

user_buget = input ("cual es tu presupuesto")

try:
    user_buget = int(user_buget)
except:
    print("porfavor ingresa un numero ")
    exit()

if user_buget >= small:
    if user_buget >= big:
        print(" te alcanza para el cafe grande")
        if user_buget == big:
            print(" pago realizado pasa ala otra ventanilla")
        else:
            print("tu cambio es: ", user_buget - big)
    elif user_buget >= regular:
        print("te alacanza para un cafe regular, para a la siguiente ")
        if user_buget == regular:
            print("pago realizado pasa ala otra ventanilla")
        else:
            print("tu cambio es ", user_buget - regular)
    elif user_buget >= small:
        print("te alcanza para un cafe chico")
        if user_buget == small:
            print("pago realizado pase ala siguiente ventanilla")
        else:
            print("tu cambio es", user_buget - small)

print("proceso finalizado")

from random import*
input ("numero del usuario")

# random = ("numero aleatorio")
# input  = ("numero del usuario")
# if input == random:
#     print("adivinaste")
# elif input > random:
#     print("es un numero menor")




secret_number = 20
number = 0
while True:
    number = int(input("adivina el numero"))
    
    if number != secret_number:
        if number > secret_number:
            print ("es mayor")
        elif number < secret_number:
            print("es menor")
        elif number == secret_number:
            print("adivinaste")

    
        

