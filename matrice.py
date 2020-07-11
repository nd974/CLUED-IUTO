# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module matrice.py
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère des matrices
"""

#--------------------
# constructeur
#--------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    matrice=[]
    for i in range(nbLignes):
        matrice.append([valeurParDefaut]*nbColonnes)
    return matrice
assert Matrice(2,3)==[[0,0,0],[0,0,0]]
assert Matrice(2,3,5)==[[5,5,5],[5,5,5]]
assert Matrice(0,0,1)==[]

#--------------------
# getters
#--------------------

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice)
assert getNbLignes([[1,2,3],[4,5,6]])==2
assert getNbLignes([[1,2],[3,4],[5,6]])==3
assert getNbLignes([])==0

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice[0])
assert getNbColonnes([[1,2,3],[4,5,6]])==3
assert getNbColonnes([[1,2],[3,4],[5,6]])==2
assert getNbColonnes([[]])==0

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice[ligne][colonne]
assert getVal([[1,2,3],[4,5,6]],1,2)==6
assert getVal([[1,2,3],[4,5,6]],0,2)==3
assert getVal([[1,2],[3,4],[5,6]],2,0)==5

#--------------------
# setters
#--------------------

def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice[ligne][colonne]=valeur

#-------------------------
# Affichage d'une matrice
#-------------------------

def afficheLigneSeparatrice(matrice,tailleCellule=4):
    ''' 
    fonction annexe pour afficher les lignes séparatrices
    paramètres: matrice la matrice à afficher
                tailleCellule la taille en nb de caractères d'une cellule
    résultat: cette fonction ne retourne rien mais fait un affichage
    '''
    print()
    for i in range(getNbColonnes(matrice)+1):
        print('-'*tailleCellule+'+',end='')
    print()
   
def afficheMatrice(matrice,tailleCellule=4):
    '''
    affiche le contenue d'une matrice présenté sous le format d'une grille
    paramètres: matrice la matrice à afficher
                tailleCellule la taille en nb de caractères d'une cellule
    résultat: cette fonction ne retourne rien mais fait un affichage
    '''
     
    nbColonnes=getNbColonnes(matrice)
    nbLignes=getNbLignes(matrice)
    print(' '*tailleCellule+'|',end='')
    for i in range(nbColonnes):
        print(str(i).center(tailleCellule)+'|',end='')
    afficheLigneSeparatrice(matrice,tailleCellule)
    for i in range(nbLignes):
        print(str(i).rjust(tailleCellule)+'|',end='')
        for j in range(nbColonnes):
            print(str(getVal(matrice,i,j)).rjust(tailleCellule)+'|',end='')
        afficheLigneSeparatrice(matrice,tailleCellule)
    print()

