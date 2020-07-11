# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module case.py
   ~~~~~~~~~~~~~~
   
   Ce module gère les cases du plateau du CLUEDO. 
"""


# constantes gérant les categories de case
# NON_CASE indique que cet emplacement du plateau n'est pas une case
# COULOIR indique les cases sont des couloirs.
# les cases dont la catégorie est supérieur à 0 sont des pièces 
# et l'entier est le numéro de la pièce en question
# les cases dont la catégorie est inférieur à 0 sont les points de départ 
# des joueurs, la valeur absolue de cette catégorie correspond au numéro du joueur

NON_CASE=None
COULOIR=0

# --------------------
# Constructeur
# ---------------------

def Case(_categorie, _contenu):
    """
    retourne une nouvelle case
    _categorie : la catégorie de la case, int ou None
    _contenu   : indique le contenu de la case. None si il n'y a pas de pion
                 sinon c'est un entier positif indiquant le numéro du joueur 
    """
    if type(_categorie) != int:
        return None
    else:
        return [_categorie, _contenu]

assert Case(None, None) == NON_CASE
assert Case(None, 0) == NON_CASE
assert Case(0, None) == [COULOIR, None]
assert Case(0, 0) == [COULOIR, 0]
assert Case(-1, 1) == [-1, 1]
assert Case(4, 4) == [4, 4]

# --------------------
# getter
# --------------------

def getCategorie(case):
    """
    retourne la catégorie de la case
    case : une case du plateau de CLUEDO 
    """
    if case == None:
        return None
    return case[0]

assert getCategorie(Case(0, None)) == COULOIR
assert getCategorie(Case(-1, 1)) == -1
assert getCategorie(Case(4, 4)) == 4

def getContenu(case):
    """
    retourne le contenu de la case
    case : une case du plateau de CLUEDO 
    """ 
    return case[1]

assert getContenu(Case(0, 0)) == 0
assert getContenu(Case(0, None)) == None
assert getContenu(Case(-1, 1)) == 1
assert getContenu(Case(-1, None)) == None
assert getContenu(Case(4, 4)) == 4

def estLibre(case):
    """
    indique si la case est libre ou non
    case : une case du plateau de CLUEDO 
    """ 
    if not case[1]:
        return True
    return False

assert estLibre(Case(COULOIR, None))
assert not estLibre(Case(-1, 1))
assert not estLibre(Case(4, 4))
assert not estLibre(Case(COULOIR, 4))
assert estLibre(Case(7, None))
assert not estLibre(Case(4, 4))
assert estLibre(Case(-9, None))

def estDepart(case):
    """
    retourne un entier 0 si la case n'est pas une case départ
    et le numéro du joueur dont c'est la case départ sinon
    case : une case du plateau de CLUEDO 
    """ 
    if case[0] < 0:
        return abs(case[0])
    return 0

assert estDepart(Case(0, 0)) == 0
assert estDepart(Case(-1, 3)) == 1
assert estDepart(Case(4, 4)) == 0
assert estDepart(Case(-6, 4)) == 6
assert estDepart(Case(-4, 4)) == 4
assert estDepart(Case(34, 4)) == 0
assert estDepart(Case(5, 0)) == 0
assert estDepart(Case(-5, 0)) == 5

# --------------------
# setters
# -------------------- 

def setContenu(case,contenu):
    """
    change le contenu de la case
    case    : une case du plateau de CLUEDO
    contenu : le nouveau contenu de la case
    """
    case[1]=contenu

def setCategorie(case, categorie):
    """
    change la catégorie de la case
    case      : une case du plateau de CLUEDO
    categorie : la nouvelle catégorie de la case
    """
    case[0]=categorie