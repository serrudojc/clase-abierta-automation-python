"""
Dada una concesionaria de autos, 5 clientes van a pedir un auto, debe preguntarsele:

*Nombre y apellido del comprador.
*Marca
*Puertas
*Color

Marcas posibles y sus precios:

-Ford $100000
-Chevrolet: $120000  
-Fiat: $80000

-Por la cantidad de puertas se añade un precio: 

-2: $50000
-4: $65000
-5: $78000

Dependiendo del color, se deben sumar:

-Blanco: $10000
-Azul: $20000
-Negro: $30000

Deben imprimirse los datos de cada compra y el precio total.
"""

marcaFord = "Ford"
marcaChevrolet = "Chevrolet"
marcaFiat = "Fiat"
precioFord = 100000
precioChevrolet = 120000
precioFiat = 80000
puertas2 = 50000
puertas4 = 65000
puertas5 = 78000
colorBlanco = 10000
colorAzul = 20000
colorNegro = 30000

for numero in range(5):
    precio = 0
    nombreYApellido = input("Ingresar nombre y apellido: ")

    marca = input("Ingresar marca: ")
    if(marca == marcaFord):
        precio = precio + precioFord
    elif(marca == marcaChevrolet):
        precio = precio + precioChevrolet
    elif(marca == marcaFiat):
        precio = precio + precioFiat
    else:
        print("No existe marca de auto")
        continue
    
    cantPuertas = int(input("Ingresar cantidad de puertas: "))
    if(cantPuertas == 2):
        precio = precio + puertas2
    elif(cantPuertas == 4):
        precio = precio + puertas4
    elif(cantPuertas == 5):
        precio = precio + puertas5
    else:
        print("No existe tal cantidad de puertas")
        continue

    color = input("ingresar color: ")
    if(color == "blanco"):
        precio = precio + colorBlanco
    elif(color == "azul"):
        precio = precio + colorAzul
    elif(color == "negro"):
        precio = precio + colorNegro
    else:
        print("No existe color")
        continue

    print("Cliente ",nombreYApellido," compró marca ",marca, cantPuertas, " puertas, color ",color,". Precio total ", precio)
