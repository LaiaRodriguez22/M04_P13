class school:
    def __init__(self, nom, any, cursos, professors, alumnes, construccio):
        self.nom = nom
        self.any = any
        self.cursos = cursos
        self.professors = professors
        self.alumnes = alumnes
        self.construccio = construccio

    # GETTERS 
    def getNom(self):
        return self.nom

    def getAny(self):
        return self.any

    def getCursos(self):
        return self.cursos

    def getProfessors(self):
        return self.professors

    def getAlumnes(self):
        return self.alumnes

    def getConstruccio(self):
        return self.construccio

    # SETTERS
    def setNom(self, nom):
        self.nom = nom

    def setAny(self, any):
        self.any = any

    def setCursos(self, cursos):
        self.cursos = cursos

    def setProfessors(self, professors):
        self.professors = professors

    def setAlumnes(self, alumnes):
        self.alumnes = alumnes

    def setConstruccio(self, construccio):
        self.construccio = construccio


    #SALUTACIO, FUNCIÓ ON ES MOSTREN TOTS ELS ATRIBUTS.
    def salutacio(self):
        print("L'institut " + self.nom + " es va inagurar l'any " + self.any + 
        ". Actualment té " + self.cursos + " cursos que imparteixen " + self.professors + 
        " professors. L'institut té capacitat per a " + self.alumnes + " alumnes." 
        + " I té diferentes construccions com un " + self.construccio);