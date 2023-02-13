class user:
    def __init__(self,nombre, apellidos, edad, año, usuario, correo): #Creación de constructor
        #Atributos añadidos al constructor
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.año = año
        self.usuario = usuario
        self.correo = correo

    #Get permite recoger la info de un atributo de la clase y devolverla
    def getnombre(self):
        return self.nombre
    #Set nos permite modificar ese atributo.
    def setnombre(self, nombre):
        self.nombre = nombre

    def getapellidos(self):
        return self.apellidos
    def setapellidos(self, apellidos):
        self.apellidos = apellidos

    def getedad(self):
        return self.edad
    def setedad(self, edad):
        self.edad = edad

    def getaño(self):
        return self.año
    def setaño(self, año):
        self.año = año

    def getusuario(self):
        return self.usuario
    def setusuario(self, usuario):
        self.usuario = usuario

    def getcorreo(self):
        return self.correo
    def setcorreo(self, correo):
        self.correo = correo

    def salutacio(self):
        print("Su nombre es " + self.nombre + ", sus apellidos son " + self.apellidos + ", su edad es:  "
              + self.edad + ", nació en el año " + self.año + ", su usuario es " + self.usuario +
              " y su correo es " + self.correo)