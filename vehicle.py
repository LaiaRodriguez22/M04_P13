class vehicle:
    def __init__(self, nom, marca, versio, any, kms, cavalls):
        self.nom = nom
        self.marca = marca
        self.versio = versio
        self.any = any
        self.kms = kms
        self.cavalls = cavalls
    
    # GETTERS 
    def getNom(self):
        return self.nom

    def getMarca(self):
        return self.marca

    def getVersio(self):
        return self.versio

    def getAny(self):
        return self.any

    def getKms(self):
        return self.kms

    def getCavalls(self):
        return self.cavalls

    # SETTERS
    def setNom(self, nom):
        self.nom = nom

    def setMarca(self, marca):
        self.marca = marca

    def setVersio(self, versio):
        self.versio = versio

    def setAny(self, any):
        self.any = any

    def setKms(self, kms):
        self.kms = kms

    def setCavalls(self, cavalls):
        self.cavalls = cavalls

    #SALUTACIO, FUNCIÓ ON ES MOSTREN TOTS ELS ATRIBUTS.
    def salutacio(self):
        print("El cotxe s'anomena " + self.nom 
        + ", pertany a la marca " + self.marca + " i és la versió " + self.versio + 
        ", que va sortir l'any " + self.any + ". Aquest cotxe porta " + self.kms + 
        " quilometres. I el motor té " + self.cavalls + " cavalls.");



