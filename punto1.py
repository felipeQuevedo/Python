class Persona:
    def __init__(self):
        self.nombre=input("Ingrese el nombre")
        self.edad=int(input("Ingrese la edad"))
        
    def Mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)




porcentaje = 3.5/100


class empleado(Persona):
    def __init__(self) :
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo:"))

    def Mostrar(self):
        super().Mostrar()
        print("sueldo: ",self.sueldo)
    

    def pagar_impuestos(self):
        if self.sueldo > 3600000:
            print("El empleado debe pagar retefuente.")
        else:
            print("El empleado no paga impuestos.")
        if self.sueldo >3600000:
         resultado= (self.sueldo*porcentaje)
         resultado1 = self.sueldo - resultado
         print("se resta ",resultado)
         print("gana",resultado1)

   
        



persona1=Persona()

empleado1=empleado()

empleado1.pagar_impuestos()