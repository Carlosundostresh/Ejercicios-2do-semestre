#Ejercicio 1
palabra = input ("ingresa una palabra papu")
contador = 0

for numero in palabra:
    contador += 1

print(f"la palabra tiene {contador} letras")

#Ejercicio 2

calificaciones = [ 88, 90, 79]

promedio = sum(calificaciones) / len(calificaciones)

print("tu promedio final es", (promedio))

#Ejercicio 3

lista_numeros = [10, 5, 43, 26, 7]
numero_grande = max(lista_numeros)

print(numero_grande)

#Ejercicio 4
lista_de_palabras = ["hola", "nachos"]
pal_grande = 0
grande =""
for palabra in lista_de_palabras:
    if pal_grande < len (palabra):
        grande = palabra
        pal_grande = len(palabra)
print("tu palabra mas grande es:" ,grande )

#Ejercicio 5

pri_numero = int(input("ingrese el primer numero"))
seg_numero = int(input("ingrese el segundo numero"))

resultado = pri_numero + seg_numero
print("tu resultado es", (resultado))

#Ejercicio 6

numero_1 = int(input("ingresa un numero"))
numero_2 = int(input("ingresa otro numero"))

resultado_2 = numero_1 - numero_2

if resultado_2 < 0:
    print("es negativo pa")
elif resultado_2 > 0: 
    print ("es positivo pa")
elif resultado_2 == 0:
    print("es cero")

#Ejercicio 7

import random

numero_random = random.randint(1,10)

numero_del_usuraio = 0

while numero_del_usuraio != numero_random:
    numero_del_usuraio = int(input("pon un numero chavalin"))
    if numero_del_usuraio < numero_random:
        print("el numero es mayor papu: ")
    elif numero_del_usuraio > numero_random:
        print("el numero es menor pa: ")
    elif numero_del_usuraio == numero_random:
        print("sera acredor de un cupon: ")

#Ejercicio 8

Lista_de_peliculas = { 
"1": "spy x family", 
"2": "Zoolander",
"3": "Digimon adventure",
"4": "Asi en la tierra como en el infierno",
"5": "Supercool"
}
int(input(f"¿Que pelicula quieres mirar?{Lista_de_peliculas}"))

if Lista_de_peliculas == 1:
    print("spy x family, clasificacion A para todo publico")
elif Lista_de_peliculas == 2:
    print("Zoolander, clasificaion B mayores de 12 años")
elif Lista_de_peliculas == 3:
    print("Digimon adventure, clasificacion A para todo publico")
elif Lista_de_peliculas == 4:
    print("Asi en la tierra como en el infierno. clasificacion B-15")
elif Lista_de_peliculas == 5 :
    print("Supercool, clasificacion C para maypres de 18 años")
    
#Ejercicio 9

peso = float(input("ingrese su peso [kg]  "))
altura = float(input("ingresa tu altura[m]  "))

imc = altura * altura / peso

if  imc <= 18.5:
    print(" bajo peso")
elif 18.5 <= 24.9: 
    print("peso normal")
elif 25 <= 29.9: 
    print("sobre peso")
elif 30 <= 34.9:
    print ("Obesidad")

#Ejercicio 10

total_de_preguntas = int(input("¿Total de preguntas del examen?"))
preguntas_correctas = int(input("¿Cuantas preguntas tiene correctas?"))
preguntas_fallidas = total_de_preguntas - preguntas_correctas
calificion_final = preguntas_correctas / total_de_preguntas * 100

print(f"tienes{preguntas_correctas}")
print(f"preguntas incorrectas{preguntas_fallidas}")
print(f"tu calificacion final es {total_de_preguntas}/100")

