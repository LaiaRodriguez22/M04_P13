class book:
    def __init__(self,nombre, autor, portada, año, edicion, genero): #Creación de constructor
        #Atributos añadidos al constructor
        self.nombre = nombre
        self.autor = autor
        self.portada = portada
        self.año = año
        self.edicion = edicion
        self.genero = genero

    # Get permite recoger la info de un atributo de la clase y devolverla
    def getnombre(self):
        return self.nombre

    # Set nos permite modificar ese atributo.
    def setnombre(self, nombre):
        self.nombre = nombre

    def getautor(self):
        return self.autor
    def setautor(self, autor):
        self.autor = autor

    def getportada(self):
        return self.portada
    def setportada(self, portada):
        self.portada = portada

    def getaño(self):
        return self.año
    def setaño(self, año):
        self.año = año

    def getedicion(self):
        return self.edicion
    def setedicion(self, edicion):
        self.edicion = edicion

    def getgenero(self):
        return self.genero
    def setgenero(self, genero):
        self.genero = genero

    def info(self):
        print("El libro se llama" + self.nombre + ", su autor es " + self.autor + ", dispone de portada "
              + self.portada + ", se publicó en el año " + self.año + ", es la edición " + self.edicion +
              " y su género es " + self.genero)