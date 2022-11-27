class alumno:
    def __init__(self,nombre,apellido,dni,edad):
        try:
            self.nombre = nombre
            self.apellido = apellido
            self.dni = dni
            self.edad = edad
        except Exception as e:
            print("Error: ",e)
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nombre):
        self.nombre = nombre