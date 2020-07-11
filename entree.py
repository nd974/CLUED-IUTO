# -*- coding: utf-8 -*-
#Landry
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module entree.py
   ~~~~~~~~~~~~~~~~
   
   Ce module gère les entrées des pièces sur le plateau. 
"""
#------------------------------------------------------#
# Constantes gérant les directions sur un plateau
#------------------------------------------------------#
NORD=0
EST=1
SUD=2
OUEST=3

#-----------------------------------------
# contructeur
#-----------------------------------------
def Entree(_direction,_ligne,_colonne):
    """
    retourne une nouvelle entrée
    _direction : direction du passage de cette entrée
    _ligne     : numéro de la ligne où se trouve l'entrée
    _colonne   : numéro de la colonne où se trouve l'entrée
    
    """
    
    return (_direction,_ligne,_colonne)
assert Entree(OUEST,1,2)==(3,1,2)
assert Entree(EST,5,2)==(1,5,2)

#-----------------------------------------
# getters
#-----------------------------------------

def getDirection(entree):
    """
    retourne la direction de l'entrée
    entree: une entrée
    """
    return entree[0]
assert getDirection((SUD,9,4))==2
assert getDirection((NORD,9,4))==0

def getLigne(entree):
    """
    retourne la ligne de l'entrée
    entree: une entrée
    """
    return entree[1]
assert getLigne((EST,3,3))==3
assert getLigne((OUEST,1,6))==1

def getColonne(entree):
    """
    retourne la colonne de l'entrée
    entree: une entrée
    """
    return entree[2]
assert getColonne((EST,1,2))==2
assert getColonne((NORD,3,3))==3
