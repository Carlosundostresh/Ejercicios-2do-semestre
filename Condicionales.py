#andamos un poco fooook

x = 1
y = 22

if x== y:
    print("verdadero")
print("brincó")

a = 5
if a > 10:
    print("si es mayor")
else:
    print("es menor")

    list = [1, 2, 3, 4]

if 2 in list:
    print("existe")
else:
    print("no existe")

# else if
    
x = 10
y = 2

if y < 0:
    result = x / y
elif y == 0:
    result = y 
else:
    result = f"no se puede dividir {x} entre {y}"
    print(result)

#condiciones anidadas

x = 28
if x < 0:
    print(f"{x} es menor que 0")
else:
    if x > 0:
        print(f"{x} es mayor que 0")
    else:
        print("x es 0")

edad = int(input("¿cuantos años tienes?"))
if edad < 18:
    print("es usted menor de edad")
else:
    print("es usted mayor de edad")
    print("salio del teibol")


#Ejercicios de la clase 1
#Primer ejercicio

primer_numero = int(input("ingresa un numero"))
segundo_numero = int(input("ingresa otro numero"))

if primer_numero> segundo_numero:
    print(f"{primer_numero} es mayor que {segundo_numero}")
else:
    print(f"{segundo_numero} es mayor que{primer_numero}")

#Segundo ejercicio

usuario = int(input("ingresa un numero"))

if usuario > 0:
    print("el numero es positivo")
else:
    if usuario < 0:
        print("el numero es negativo")
        
#Tercer ejercicio
        
calificacion = int(input("ingresa una calificacion"))

if calificacion == 100:
    print("tu calificacion es A")
elif calificacion>= 90:
    print("tu calificacion es B")
elif calificacion>= 80:
    print("tu calificacion es C")
elif calificacion>= 70:
    print("tu calificacion es D")
elif calificacion>= 60:
    print("tu calificacion es F")

#Cuarto ejercicio

usuario_2 =int(input("pon un numero chaval"))

if(usuario_2 % 2 == 0):
    print("el numero es par")
else:
    print("el numero es impar")
  