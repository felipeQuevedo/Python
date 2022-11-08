class Alumno:
    def __init__(self) :
        self.nombre=input("Ingrese el nombre")
        self.nota=float(input("Ingrese la nota"))


    def Mostrar(self):
        print( "Nombre",self.nombre)
        print("Nota",self.nota)
        print(self.nota)
class estudiante(Alumno):
    def __init__(self) :
        super().__init__()
        self.sueldo=float(input("Ingrese la nota:"))
    def Mostrar(self):
        super().Mostrar()
        print("nota: ",self.nota)


class alumno1(Alumno):
    def calificaciones(self):
        if self.nota >= 3:
            print("Aprobo")
        else:
            print("No aprobo")


           
estudiante1=Alumno()
estudiante2=alumno1()
estudiante2.calificaciones()


