# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module mystere.py
   ~~~~~~~~~~~~~~~
   
   Ce module gère un mystère c'est à dire les trois cartes à deviner.
"""
import carte

#------------------
# constructeur
#------------------
def Mystere(_numProf,_numMat,_numSalle):
    """
    retourne un nouveau mystère défini par les trois numéros de cartes passés paramètres
    _numProf  : numero du professeur
    _numMat   : numéro de la matière
    _numSalle : numéro de la salle
    """
    return (_numProf,_numMat,_numSalle)

assert Mystere(7,5,9)==(7,5,9)
assert Mystere(2,3,4)==(2,3,4)



#------------------
# getters
#------------------

def getProfesseur(mystere):
    """
    retourne le numéro du professeur du mystère
    mystere: un mystere
    """
    return mystere[0]

assert getProfesseur((7,5,9))==7
assert getProfesseur((2,3,4))==2




def getMatiere(mystere):
    """
    retourne le numéro de la matières du mystère
    mystere: un mystere
    """
    return mystere[1]

assert getMatiere((7,5,9))==5
assert getMatiere((2,3,4))==3




def getSalle(mystere):
    """
    retourne le numéro de la salle du mystère
    mystere: un mystere
    """
    return mystere[2]

assert getSalle((7,5,9))==9
assert getSalle((2,3,4))==4