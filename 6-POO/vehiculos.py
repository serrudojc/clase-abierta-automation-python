class Vehiculo():
    def __init__(self,color,marca,velocidad_maxima):
        self.color = color
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def encender_auto(self):
        self.encendido = True
        print('Auto Encendido')

    def apagar_auto(self):
        self.encendido = False
        print('Auto Apagado')

    def mostrar_velocimetro(self):
        print('La velocidad actual es de '+str(self.velocidad_actual)+' de '+str(self.velocidad_maxima))
    
    def acelerar(self,velocidad):
        if(self.encendido == True):
            if(self.velocidad_actual + velocidad >= self.velocidad_maxima):
                self.velocidad_actual = self.velocidad_maxima
            else:
                self.velocidad_actual = self.velocidad_actual + velocidad
        else:
            print('El auto está apagado')
        self.mostrar_velocimetro()

    def frenar(self, velocidad):
        if(self.velocidad_actual - velocidad < 0):
            self.velocidad_actual = 0
        else:
            self.velocidad_actual = self.velocidad_actual - velocidad
        self.mostrar_velocimetro()


class Camion(Vehiculo):
    def __init__(self, carga_maxima,color,marca,velocidad_maxima):
        self.carga_maxima = carga_maxima
        self.carga_actual = 0
        Vehiculo.__init__(self,color,marca,velocidad_maxima)

    def cargar(self,cantidad):
        self.carga_actual = self.carga_actual + cantidad

    def mostrar_velocimetro(self):
        print('La velocidad actual es de '+str(self.velocidad_actual)+' de '+str(self.velocidad_maxima)+' Y la carga es '+str(self.carga_actual))

class Automovil(Vehiculo):
    def __init__(self, puertas, color, marca, velocidad_maxima):
        self.puertas = puertas
        Vehiculo.__init__(self,color,marca,velocidad_maxima)
    
    def abrir_puertas(self, nro_puertas):
        print('Se abren las puertas')


mi_auto = Automovil(4,'Verde', 'Peugeot', 180)
mi_auto.encender_auto()
mi_auto.acelerar(50)
#print(mi_auto.color)
#mi_auto.mostrar_velocimetro()

#mi_auto.encender_auto()
#mi_auto.acelerar(80)
#mi_auto.acelerar(1000)
#mi_auto.frenar(50)
#mi_auto.apagar_auto()


mi_camion = Camion('Scania','azul',120,2000)
mi_camion.encender_auto()
mi_camion.acelerar(20)
mi_camion.mostrar_velocimetro()
#mi_camion.carga_actual = 500
#mi_camion.acelerar(100)
#print(mi_camion.carga_actual)
