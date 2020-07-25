# Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
# Se pide imprimir el nombre, el apellido y el promedio.
# Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". Caso 
# contrario, si tiene menos de 4 puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 
# imprimir "A recuperatorio".
# En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".


nombreApellido = input("Ingresar nombre y apellido: ")
notaMatematica = int(input("Ingresar nota de matemática: "))
notaLiteratura = int(input("Ingresar nota de literatura: "))
notaFisica = int(input("Ingresar nota de fisica: "))

promedio = (notaMatematica + notaLiteratura + notaFisica)/3
print("Alumno: ",nombreApellido, ". Promedio: ",promedio)