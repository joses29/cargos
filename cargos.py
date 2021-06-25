class Cargo:
    secuencia=0
    def __init__(self,cod=0,des=""):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        self.descripcion=des

cargo1 = Cargo()
cargo1.codigo=1
cargo1.descripcion="Docente"
print(cargo1.codigo,cargo1.descripcion)
cargo2 = Cargo()
cargo2.codigo=2
cargo2.descripcion="Director"
print(cargo2.codigo,cargo2.descripcion)
cargo3 = Cargo(3,"Analista")
print(cargo3.codigo,cargo3.descripcion)
print(Cargo.secuencia)
print(cargo1.secuencia)
print(cargo2.secuencia)
print(cargo3.secuencia)


# Empleados 

from cargos import Cargo

class Empleado:
    secuencia=0
    def __init__(self,nom,ced,sue,cargo):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=cargo
    def mostrar(self):
        print("codigo:{} nombre:{} cargo:{}-{}".format(self.codigo,self.nombre,self.cargo.codigo,self,cargo,descripcion))

    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia

cargo1 = Cargo("Docente")
emp1= Empleado("Maryuri","9870",500,cargo1)
emp1.mostrar()
cargo2= Cargo("Analisis")
emp2= Empleado("jose","8754",500,cargo2)
emp2.mostrar()






