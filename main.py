# IMPORTS DE ARXIUS
from animal import animal
from vehicle import vehicle
from school import school
from book import book
from user import user
from university import university

#INTEGRANT A -- LAIA RODRÍGUEZ RAMOS

print("INTEGRANT A -- LAIA RODRÍGUEZ RAMOS")
#ANIMAL
#------------1
an1 = animal("Lynx", "7", "mamifers", "felins", "Àsia Central", "quatre")
an1.salutacio()
an1.setHabitat("Estats Units")
an1.salutacio()
#------------2
an2 = animal("Llop", "", "mamifers", "canis lupus", "Estats Units i Canadà", "quatre")
an2.salutacio()
an2.setEdat("8")
an2.salutacio()

#VEHICLE
#------------1
veh1 = vehicle("Grand Chokke", "Jeep", "3", "2003", "167.000", "144")
veh1.salutacio()
veh1.setNom("Grand Cherokee")
veh1.salutacio()
#------------2
veh2 = vehicle("Renegade", "Jeep", "1", "1999", "33.000", "220")
veh2.salutacio()
veh2.setCavalls("454")
veh2.salutacio()

#ESCOLA
#------------1
sc1 = school("Jaume Balmes" , "1956", "35", "76", "432", "jardi botanic")
sc1.salutacio()
sc1.setAny("1899")
sc1.salutacio()
#------------2
sc2 = school("INS Palamós" , "1944", "20", "47", "235", "gimnàs")
sc2.salutacio()
sc2.setCursos("10")
sc2.salutacio()


#INTEGRANT B -- ALEX NAVARRO RODRÍGUEZ

print("INTEGRANT A -- ALEX NAVARRO RODRÍGUEZ")

#BOOK
#------------1
book1 = book ("Geronimo Stilton", " Un ratón ", " blanda ", " 2002 " , " 2ª ", " Novela fantasía")
book1.info()
book1.setautor(" dos ratones ")
book1.info()
#------------2
book2 = book ("Geronima Stiltona", " Un perro ", " dura ", " 2008 " , " 8ª ", " Novela fantasía")
book2.info()
book2.setaño(" 2013")
book2.info()

#USER
#------------1
user1 = user ("Alex", " Navarro Rodríguez ", " 23 años", " 1999 " , " alexitocalipo ", " alexitocalipo2@gmail.com")
user1.salutacio()
user1.setedad(" 24 años")
user1.salutacio()

#------------2
user2 = user ("Eric", " Navarro Rodríguez ", " 28 años", " 1995 " , " ericus1 ", " ericus1@hotmail.com")
user2.salutacio()
user2.setaño(" 1994 ")
user2.salutacio()

#UNIVERSITAT
#------------1
university1 = university ("UAB", " Plaça Cívica", " 185000 alumnos ", " 89 " , " Patricia " , " 93822")
university1.info()
university1.setnombre("UB")
university1.info()

#------------2
university2 = university ("UPC", " Calle Gorila 21 ", " 893742 alumnos ", " 74 " , " David " , " 41222")
university2.info()
university2.setcapacidad("124852 alumnos")
university2.info()