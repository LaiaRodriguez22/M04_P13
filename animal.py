class animal:
    def __init__(self, nom, edat, especie, familia, habitat, potes):
        self.nom = nom
        self.edat = edat
        self.especie = especie
        self.familia = familia
        self.habitat = habitat
        self.potes = potes

    # GETTERS 
    def getNom(self):
        return self.nom

    def getEdat(self):
        return self.edat

    def getEspecie(self):
        return self.especie

    def getFamilia(self):
        return self.familia

    def getHabitat(self):
        return self.habitat

    def getPotes(self):
        return self.potes

    # SETTERS
    def setNom(self, nom):
        self.nom = nom

    def setEdat(self, edat):
        self.edat = edat

    def setEspecie(self, especie):
        self.especie = especie

    def setFamilia(self, familia):
        self.familia = familia

    def setHabitat(self, habitat):
        self.habitat = habitat

    def setPotes(self, potes):
        self.potes = potes

    #SALUTACIO, FUNCIÓ ON ES MOSTREN TOTS ELS ATRIBUTS.
    def salutacio(self):
        print("L'animal que us presento és diu " + self.nom + ". Pot arribar a tenir " + self.edat + " anys."  +
        " Pertany a l'especie " + self.especie + " i dintre d'aquesta, forma part de la familia " + self.familia +
        ". Aquest animal viu en varies zones com " + self.habitat + ". Per acabar, té " + self.potes + " potes.");