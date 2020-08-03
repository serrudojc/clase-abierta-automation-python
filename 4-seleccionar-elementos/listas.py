# listas
autos = ['Ford','Chevrolet','Fiat']
print(autos)
print(autos[2])
print(autos[-2])    # puedo recorrer las lista de atras para adelante
print(autos[0:2])

autos.append('Dodge')
print(autos)

autos.insert(1,'Ferrari')
print(autos)

del autos[2]
print(autos)

print(len(autos))

autos[2] = 'Ika'
print(autos)


# tuplas
colores = ('amarillo','azul','verde')
print(colores)

print('amarillo' in colores)


# diccionarios
usuario = {'id':1, 'name':'pedro','age':37}
print(usuario['name'])

usuario['name'] = 'Nancy Tupla'
print(usuario)

usuario['apellido'] = 'algo'
print(usuario)

del usuario['apellido']
print(usuario)

print(usuario.keys())

print(usuario.values())

