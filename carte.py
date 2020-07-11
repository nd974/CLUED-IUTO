# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module carte.py
   ~~~~~~~~~~~~~~~
   
   Ce module gère les cartes du Cluedo. Une carte fait partie d'une des trois catégorie (professeur,matière,salle)
   Elle porte un nom et elle possède une description et une image
"""

# constantes permettant de définir les trois catégorie de carte
PROFESSEUR=1
MATIERE=2
SALLE=3
# variable pour les tests
test_carte=(2,"Base de donnée",MATIERE,"Stockage et interrogation des données",True)
test_carte2=(3,"i23",SALLE,"Salle de machine à l'étage",False)
test_carte3=(4,"Jrad",PROFESSEUR,"Prof de AP",True)
# Dictionaire qui contient les noms des catégories
nomCategorie={PROFESSEUR:"Professeurs",MATIERE:"Matières",SALLE:"Salles"}

#-----------------------------------------
# contructeur
#-----------------------------------------
def Carte(_num,_nom,_categorie,_description,_distribuable=True):
    """
    retourne une carte du CLuedo
    _num        : numéro de la carte
    _nom        : nom de la carte
    _categorie  : catégorie de la carte (parmi PROFESSEUR, MATIERE, SALLE
    _description: une chaine de caractères contenant la description de la carte
    _distribuable: un booléen indiquant si la carte est distribuable ou non
    """
    return (_num,_nom,_categorie,_description,_distribuable)
assert Carte(2,"Base de donnée",MATIERE,"Stockage et interrogation des données")
assert Carte(3,"i23",SALLE,"Salle de machine à l'étage",False)==test_carte2

#-----------------------------------------
# accesseurs
#-----------------------------------------
def getNum(carte):
    """
    retourne le numéro d'une carte du Cluedo
    carte: une carte du Cluedo
    """
    return carte[0]
assert getNum(test_carte)==2
assert getNum(test_carte2)==3

def getNom(carte):
    """
    retourne le nom d'une carte du Cluedo
    carte: une carte du Cluedo
    """
    return carte[1]
assert getNom(test_carte)=="Base de donnée"
assert getNom(test_carte2)=="i23"

def getCategorie(carte):
    """
    retourne la catégorie d'une carte du Cluedo
    carte: une carte du Cluedo
    """
    return carte[2]
assert getCategorie(test_carte)==MATIERE
assert getCategorie(test_carte2)==SALLE

def getNomCategorie(carte): 
    """
    retourne le nom de la catégorie d'une carte du Cluedo
    carte: une carte du Cluedo
    """
    return nomCategorie[getCategorie(carte)]
assert getNomCategorie(test_carte)=="Matières"
assert getNomCategorie(test_carte2)=="Salles"

def getDescription(carte):
    """
    retourne la description d'une carte du Cluedo
    carte: une carte du Cluedo
    """
    return carte[3]
assert getDescription(test_carte)=="Stockage et interrogation des données"
assert getDescription(test_carte2)=="Salle de machine à l'étage"

def estDistribuable(carte):
    """
    indique si une carte est distribuable ou non
    carte: une carte du Cluedo
    """
    return carte[4]
assert estDistribuable(test_carte)
assert not estDistribuable(test_carte2)


#-------------------------
# fonctions annexes
#-------------------------
def categorieFromNom(nomCat):
    """
    retourne l'identifiant d'un nom de catégorie 
    nomCart: un nom de catégorie
    """
    for (ident,nom) in nomCategorie.items():
        if nomCat==nom:
            return ident
assert categorieFromNom("Matières")==MATIERE
assert categorieFromNom("Salles")==SALLE
assert categorieFromNom("Professeurs")==PROFESSEUR

def categorieFromNum(numCat):
    """
    retourne le nom d'une carte du Cluedo
    numCat: un identifiant de catégorie
    """
    return nomCategorie[numCat]
assert categorieFromNum(2)=="Matières"
assert categorieFromNum(1)=="Professeurs"
assert categorieFromNum(3)=="Salles"

def estNomCategorie(nomCat):
    """
    indique si une chaine de caractères est un nom de catégorie ou non
    nomCat: un nom de catégorie
    """
    for nom in nomCategorie.values():
        if nomCat==nom:
            return True
    return False
assert estNomCategorie("Matières")
assert not estNomCategorie("Livre")
assert not estNomCategorie("")

#-------------------------
# transformer une carte en chaine de caractères
#-------------------------
def string(carte):
    """
    retourne une chaine de caractères représentant une carte du Cluedo
    carte: une carte du Cluedo
    """
    return '-'*10+'\ncarte '+getNomCategorie(carte)+' numéro: '+str(getNum(carte))+'\nnom: '+getNom(carte)+'\ndescription: '+getDescription(carte)+'\n'

