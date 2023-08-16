from Proyecto.dominio.persona import Persona1
# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana,
# Mieles Piloso Andrews, Vera Saltos Jimmy


class Estudiante(Persona1):
    contador_estudiante = 0

    def __init__(self, cedula: str = None, nombre: str = None, apellido: str = None, email: str = None,
                 telefono: str = None, direccion: str = None, carrera: str = None, numero_libros: int = 0,
                 activo: bool = True, nivel: int = 0, fecha_nacimiento: int = None, edad: int = None,
                 estatura: int = None, peso: int = None):
        super().__init__(cedula=cedula, nombre=nombre, apellido=apellido, email=email, telefono=telefono,
                         direccion=direccion, carrera=carrera, numero_libros=numero_libros, activo=activo,
                         fecha_nacimiento=fecha_nacimiento, edad=edad, estatura=estatura, peso=peso)
        Estudiante.contador_estudiante += 1
        self._id = Estudiante.contador_estudiante
        self._nivel = nivel

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    def pedir_libro(self):
        if self.activo and self.numero_libros < 3:
            self.numero_libros += 1
            return True
        return False

    def devolver_libro(self):
        if self.activo and self.numero_libros > 0:
            self.numero_libros -= 1
            return True
        return False

    def __str__(self):
        return (f"Id: {self._id}\nCédula: {self._cedula}\nNombre: {self._nombre}\nApellido: {self._apellido}\n"
                f"Email: {self._email}\nCarrera: {self._carrera}\nActivo: {self._activo}\n"
                f"Fecha Nacimiento: {self._fecha_nacimiento}\nEdad: {self._edad}\nEstatura: {self._estatura}\n"
                f"Peso: {self._peso}")


if __name__ == '__main__':
    est1 = Estudiante(cedula="0123456789", nombre="Pablo", apellido="Pérez", email="pablo@gmail.com",
                      telefono="0960354278", direccion="Francisco de Orellana", carrera="Ingeniería", numero_libros=2,
                      activo=True, nivel=2)
    est2 = Estudiante(cedula="0987456123", nombre="Luisa", apellido="López", email="luisa@gmail.com",
                      telefono="0936157689", direccion="Avenida Sixto Garay", carrera="Medicina",
                      numero_libros=4, activo=False, nivel=3)
    print('*'.center(100, '*'))
    print(est1)
    print('*'.center(100, '-'))
    print(est2)

