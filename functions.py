# number_a = 5

# def operation_addition(number_b):
#     return number_a + number_b

# def operation_substract(number_b):
#     return number_a - number_b

# def greet(name):
#     return "Hola " + name

# result = greet("Carlos")
# print(result)

#Multiplicacion

numero_1 = 40

def operacion_multiplicacion(numero_2):
    return numero_1 * numero_2
result = operacion_multiplicacion (20)
print(result)

#Division
def operacion_division(numero_2):
    return numero_1 / numero_2
result = operacion_division (50)
print(result)

#Exponencial
def operacion_expo(numero_2):
    return numero_1**numero_2
result= operacion_expo (18)
print(result) 

#Hacer una funcion donde manden 3 parametros,
#el primero y el segundo seran numeros y
#el tercero sera el tipo de operacion que quieres realizar.

#Si la operacion es suma, sumaran y regresaras el resultado imprimirlo.
#el mismo caso para la resta, division, multiplicacion y potencia

def operacion (numero_1, numero_2, operacion):
    if operacion == "suma":
        return numero_1 + numero_2
    elif operacion == "resta":
        return numero_1 - numero_2
    elif operacion == "multiplicacion":
        return numero_1 * numero_2
    elif operacion == "division":
        return numero_1 / numero_2
    else:
        print ("operacion invalida")
result = operacion (5, 8, "division")
print(f"el resultado es {result}")
