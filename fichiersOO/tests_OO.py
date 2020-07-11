import carteOO 
import mystere00

#tests carteOO

c1=carteOO.Carte(2,"Base de donnée",carteOO.MATIERE,"Stockage et interrogation des données",True)
c2=carteOO.Carte(3,"i23",carteOO.SALLE,"Salle de machine à l'étage",False)

#getteur
assert carteOO.Carte.getNum(c1)==2
assert carteOO.Carte.getNum(c2)==3

assert carteOO.Carte.getNom(c1)=='Base de donnée'
assert carteOO.Carte.getNom(c2)=='i23'

assert carteOO.Carte.getCategorie(c1)==2
assert carteOO.Carte.getCategorie(c2)==3

assert carteOO.Carte.getNomCategorie(c1)=="Matières"
assert carteOO.Carte.getNomCategorie(c2)=='Salles'

assert carteOO.Carte.getDescription(c1)=="Stockage et interrogation des données"
assert carteOO.Carte.getDescription(c2)=="Salle de machine à l'étage"

assert carteOO.Carte.estDistribuable(c1)
assert not carteOO.Carte.estDistribuable(c2)


#fonction annexe
assert carteOO.categorieFromNom("Professeurs")==1
assert carteOO.categorieFromNom("Matières")==2

assert carteOO.categorieFromNum(carteOO.PROFESSEUR)=="Professeurs"
assert carteOO.categorieFromNum(carteOO.SALLE)=="Salles"

assert carteOO.estNomCategorie("Professeurs")
assert not carteOO.estNomCategorie("Ruisseau")

#tests mystere00

m1=mystere00.Mystere(2,5,5)
m2=mystere00.Mystere(3,4,2)

assert mystere00.Mystere.getProfesseur(m1)==2
assert mystere00.Mystere.getProfesseur(m2)==3

assert mystere00.Mystere.getMatiere(m1)==5
assert mystere00.Mystere.getMatiere(m2)==4

assert mystere00.Mystere.getSalle(m1)==5
assert mystere00.Mystere.getSalle(m2)==2

