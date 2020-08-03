class Automovil():
    def __init__(self, color, marca, velocidad_maxima):
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



mi_auto = Automovil('Verde', 'Peugeot', 180)
print(mi_auto.color)
mi_auto.mostrar_velocimetro()

mi_auto.encender_auto()
mi_auto.acelerar(80)
mi_auto.acelerar(1000)
mi_auto.frenar(50)
mi_auto.apagar_auto()
