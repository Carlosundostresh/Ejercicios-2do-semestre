# bucle while

numer = 0 
while numer <= 10:
    print(f"{numer * 3}")
    numer += 1
print("he finalizado la tabla del 3")

values = [5, 1, 9, 2, 7, 4]

found = False
index = 0
value_to_find = 7
longitud = len (values)

while not found and index < longitud:
    value = values [index]
    if value == value_to_find:
        found = True
    else:
        index += 1

if found:
    print(f"el numero {value_to_find} ha sido encontrado en el indice")
else:
    print(f"el numero {value_to_find} no se encuentra en la lista")

array = ["a","b","c","d","e","f",]

for letter in array:
    print(f"dame la letra actual: {letter}")
    if letter == "d":
        print("se encontro la letra e")
        break

letra = "v"
letra = input("ingresa algo")
for palabra in letra:
    print(f"dame algo {palabra} ")
    if palabra == "v":
        print("se encontro") 





    