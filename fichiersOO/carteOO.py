# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module carteOO.py
   ~~~~~~~~~~~~~~~
   
   Ce module gère les cartes du Cluedo. Une carte fait partie d'une des trois catégorie (professeur,matière,salle)
   Elle porte un nom et elle possède une description et une image
"""

# constantes permettant de définir les trois catégorie de carte
PROFESSEUR=1
MATIERE=2
SALLE=3


# Dictionaire qui contient les noms des catégories
nomCategorie={PROFESSEUR:"Professeurs",MATIERE:"Matières",SALLE:"Salles"}


class Carte(object):
    def __init__(self,_num,_nom,_categorie,_description,_distribuable=True):
        """
        constructeur
        """
        self._num=_num
        self._nom=_nom
        self._categorie=_categorie
        self._description=_description
        self._distribuable=_distribuable

    #accesseur
    def getNum(self):
        return self._num


    def getNom(self):
        return self._nom

    def getCategorie(self):
        return self._categorie

    def getNomCategorie(self):
        return nomCategorie[self._categorie]


    def getDescription(self):
        return self._description


    def estDistribuable(self):
        return self._distribuable
    
    def string(self):
        return '-'*10+'\ncarte '+getNomCategorie(self)+' numéro: '+str(getNum(self))+'\nnom: '+getNom(self)+'\ndescription: '+getDescription(self)+'\n'
 

#fonction annexe
def categorieFromNom(nomCat):
    for (ident,nom) in nomCategorie.items():
        if nomCat==nom:
            return ident


def categorieFromNum(numCat):
    return nomCategorie[numCat]


def estNomCategorie(nomCat):
    for nom in nomCategorie.values():
        if nomCat==nom:
            return True
    return False


# transformer une carte en chaine de caractères

