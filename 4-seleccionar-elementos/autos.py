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

Dado el problema anterior del concesionario de autos debemos modificarlo, teniendo en cuenta:

1-Ya no sabemos cuantos clientes tendremos, 
2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
3-Lo mismo con la cantidad de puertas y los colores.
4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
5-Si la cantidad de clientes fue:
--5.1: 0 a 5 personas no hay descuento
--5.2: 6 a 10 personas: hay un descuento del 10%
--5.3: 11 a 50 personas: hay un descuento del 15%
--5.4: Más de 50 personas: El descuento es del 18%
6-Solo se va a mostrar que se vendió al final del programa

"""

autosPrecio = {'Ford':100000, 'Chevrolet':120000, 'Fiat':80000}
puertasPrecio = {'2':50000, '4':65000,'5':78000}
colorPrecio = {'blanco':10000, 'azul':20000,'negro':30000}
clientes =  {}

contadorClientes = 0
continuar = True

while(continuar):
    nombreYApellido = input("Ingresar nombre y apellido: ")
    precio = 0
    
    ciclo = True
    while(ciclo):
        marca = input("Ingresar marca: ")
        if(marca in autosPrecio):
            precio = precio + autosPrecio[marca]
            ciclo = False

    ciclo = True
    while(ciclo):
        puerta = input("Ingresar puertas: ")
        if(puerta in puertasPrecio):
            precio = precio + puertasPrecio[puerta]
            ciclo = False

    ciclo = True
    while(ciclo):
        color = input("Ingresar color: ")
        if(color in colorPrecio):
            precio = precio + colorPrecio[color]
            ciclo = False 

    contadorClientes += 1
    clientes[nombreYApellido] = [precio]
    otroCliente = input("Ingresar otro cliente? [y][n]: ")
    if(otroCliente != 'y'):
        continuar = False

print(clientes)