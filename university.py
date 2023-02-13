class university:
    def __init__(self,nombre, direccion, capacidad, profesores, director, alumnos): #Creación de constructor
        # Atributos añadidos al constructor
        self.nombre = nombre
        self.direccion = direccion
        self.capacidad = capacidad
        self.profesores = profesores
        self.director = director
        self.alumnos = alumnos

    # Get permite recoger la info de un atributo de la clase y devolverla
    def getnombre(self):
        return self.nombre

    # Set nos permite modificar ese atributo.
    def setnombre(self, nombre):
        self.nombre = nombre

    def getdireccion(self):
        return self.direccion
    def setdireccion(self, direccion):
        self.direccion = direccion

    def getcapacidad(self):
        return self.capacidad
    def setcapacidad(self, capacidad):
        self.capacidad = capacidad

    def getprofesores(self):
        return self.profesores
    def setprofesores(self, profesores):
        self.profesores = profesores

    def getdirector(self):
        return self.director
    def setdirector(self, director):
        self.director = director

    def getalumnos(self):
        return self.alumnos
    def setalumnos(self, alumnos):
        self.alumnos = alumnos

    def info(self):
        print("La universidad se llama  " + self.nombre + ", su dirección es  " + self.direccion + ", dispone de una capacidad de :  "
              + self.capacidad + " alumnos " +  ", tiene un total de " + self.profesores + " profesores,  " +
              " su director es " + self.director + ", y un total de " + self.alumnos + " matriculados actualmente")