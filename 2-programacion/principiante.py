# if
edad = 17
if(edad > 18):
    print("Ud es mayor de edad")
else:
    print("Ud es menor de edad")



# if multiple
valor = 3
if valor == 1:
    print("Gano x")
elif valor == 2:
    print("Ganó Y")
elif valor == 3:
    print("Ganó z")
elif valor == 4:
    print("gano w")
else:
    print("no ganó nada")



# for
for numero in range(11):
    print(numero)
print("")

for numero in range(20,30):
    print(numero)
print("")

for numero in range(40,60,2):
    print(numero)
print("")

for numero in range(20,10,-2):
    print(numero)
print("")



# while
contador = 0
condicion = True
while condicion:
    contador = contador + 1
    if(contador == 10):
        condicion = False
    print(contador, " dentro del while")


# Entrada de datos

edad = input("Ingrese su edad: ")   #SIEMPRE INGRESA STRING
print(edad)
edad = int(edad) #CAST
print(edad+5)

print("sumar "+"strings "+" = "+"es concatenar")


# funciones
def ingresar_numero():
    numero = input("Ingrese numero: ")
    print("variable numero dentro de la funcion",int(numero)+20)
    return numero

mi_numero = ingresar_numero()
print("variable numero fuera de la funcion: ",mi_numero)


def hacer_algo_con_numeros(a, b):
    return a + b

a = 50
b = 20
mi_variable = hacer_algo_con_numeros(a, b)
print(mi_variable)