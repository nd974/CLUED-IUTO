# -*- coding: utf-8 -*-
"""
						   Projet CLUED'IUTO 
		Projet Python 2018 de 1ere année DUT Informatique Orléans
		
   Module piece.py
   ~~~~~~~~~~~~~~~
   
   Ce module gère les pièces dans lesquelles peuvent se dérouler un cours. 
   Une pièce possède un numéro, une liste d'entrées, un contenu
   une liste de numeros de joueurs et éventuellement un passage secret 
"""

import entree


#-----------------------------------------
# variables pour tests
#-----------------------------------------

piece0 = [0, set(), set(), None]
piece1 = [56, {(entree.OUEST,1,2)}, {0,2,1,6,5}, (42,18,27)]
piece2 = [42, {(entree.OUEST,1,2),(entree.EST,5,2),(entree.OUEST,1,4)}, {1}, (5,10,3)]

#-----------------------------------------
# contructeur
#-----------------------------------------

def Piece(_numPiece):
	"""
	retourne une nouvelle pièce vide dont on ne connait que le numéro
	les autres informations seront remplies grâces au setters
	_numPiece : le numéro de la pièce créée 
	"""
	listeEntrees = set()
	contenu = set()
	passage = None
	piece = [_numPiece, listeEntrees, contenu, passage]
	return piece
assert Piece(0) == [0,set(),set(),None]
assert Piece(1) == [1,set(),set(),None]
assert Piece(2) == [2,set(),set(),None]


#-----------------------------------------
# getters
#-----------------------------------------

def getNum(piece):
	"""
	retourne le numéro de la pièce
	piece : une piece
	"""
	return piece[0]

assert getNum(piece0) == 0
assert getNum(piece1) == 56
assert getNum(piece2) == 42


def getListeEntrees(piece):
	"""
	retourne l'ensemble des entrées d'une pièce
	piece : une piece
	"""
	return piece[1]

assert getListeEntrees(piece0) == set()
assert getListeEntrees(piece1) == {(entree.OUEST,1,2)}
assert getListeEntrees(piece2) == {(entree.OUEST,1,2),(entree.EST,5,2),(entree.OUEST,1,4)}


def getContenu(piece):
	"""
	retourne le contenu de la pièce l'ensemble des numéros des joueurs qui s'y trouvent
	piece : une piece
	"""
	return piece[2]

assert getContenu(piece0) == set()
assert getContenu(piece1) == {0,1,2,5,6}
assert getContenu(piece2) == {1}


def getPassage(piece):
	"""
	retourne le numéro de la pièce vers laquelle on peut aller grâce au passage secret de la pièce
			  None si la pièce ne possède pas de passage secret
	piece : une piece
	"""
	passage = piece[3]
	if passage !=None:
		return passage[0]


def getEntreesDirection(piece,direction):
	"""
	retourne l'ensemble des entrées de la pièce qui permettent
	d'y entrer dans la direction indiquée en paramètre
	piece : une piece
	direction: direction par où on essaie d'entrer
	"""
	listeEntrees = getListeEntrees(piece)
	ensembleEntreesDirection = set()
	for entrees in listeEntrees:
		directionEntree = entree.getDirection(entrees)
		if directionEntree == direction:
			ensembleEntreesDirection.add(entrees)
	return ensembleEntreesDirection

assert getEntreesDirection(piece0,entree.NORD) == set()
assert getEntreesDirection(piece1,entree.OUEST) == {(entree.OUEST,1,2)}
assert getEntreesDirection(piece1,entree.NORD) == set()
assert getEntreesDirection(piece2,entree.OUEST) == {(entree.OUEST,1,2),(entree.OUEST,1,4)}


#-------------------------
# setters et modificateurs
#-------------------------

def setPassage(piece,pieceDestination, lig, col):
	"""
	modifie le passage secret de la pièce
	piece            : une piece
	pieceDestination : le numero de la pièce que l'on accède via le passage secret
	lig              : le numéro de la ligne où se trouve le passage secret
	col              : le numéro de la colonne où se trouve le passage secret
	"""
	piece[3] = (pieceDestination, lig, col)

setPassage(piece0,56,10,3)
assert piece0[3] == (56,10,3)
setPassage(piece1,14,70,16)
assert piece1[3] == (14,70,16)
	

def addEntree(piece,entree):
	"""
	ajoute une entrée à la pièce
	piece  : une piece
	entree : une entree (du type décrit dans le fichier entree.py)
	"""
	piece[1].add(entree)

entreePiece0=entree.Entree(entree.NORD,4,5)
addEntree(piece0, entreePiece0)
assert getListeEntrees(piece0) == {entreePiece0}
entreePiece1=entree.Entree(entree.SUD,3,9)
addEntree(piece1, entreePiece1)
assert getListeEntrees(piece1) == {(entree.OUEST,1,2),entreePiece1}


def addJoueur(piece,numJoueur):
	"""
	ajoute un joueur au contenu de la pièce
	piece  : une piece
	numJoueur : un numéro de joueur
	"""
	piece[2].add(numJoueur)

addJoueur(piece0, 3)
assert getContenu(piece0) == {3}
addJoueur(piece1, 3)
assert getContenu(piece1) == {0,1,2,3,5,6}


def enleverJoueur(piece,numJoueur):
	"""
	enlève un joueur du contenu de la pièce. Si le joueur n'existe pas peut provoquer une erreur
	piece  : une piece
	numJoueur : un numéro de joueur
	"""
	piece[2].remove(numJoueur)

enleverJoueur(piece1, 1)
assert getContenu(piece1) == {6,5,2,0,3}
	

def estEntree(piece,lig,col):
	"""
	indique si une des entrées de la pièce se trouve en lig,col
	piece  : une piece
	lig    : un numéro de ligne
	col    : un numéro de colonne
	"""
	listeEntrees = getListeEntrees(piece)
	for entrees in listeEntrees:
		ligneEntree = entree.getLigne(entrees)
		colonneEntree = entree.getColonne(entrees)
		if lig == ligneEntree and col == colonneEntree:
			return True
	return False

assert not estEntree(piece2, 99,2)
assert estEntree(piece2, 1,2)


def estPassage(piece,lig,col):
	"""
	indique si le passage secret se trouve en lig,col
	la fonction retourne 0 si ce n'est pas le cas et 
	le numéro de la pièce destination sinon
	###piece  : une piece
	lig    : un numéro de ligne
	col    : un numéro de colonne
	"""
	passage = piece[3]
	if passage==None:
		return 0
	lignePassage = passage[1]
	colonepassage = passage[2]
	if lig == lignePassage and col == colonepassage:
		return passage[0]
	return 0

assert not estPassage(piece2, 10,2)
assert estPassage(piece2,10,3) == 5


#demander si plusieurs passages possibles
#demander si on peut enlever un passage
#demander si on peut enlever une entrée
#demander si un passage amène forcement au passage qui y amène
#demander quelle piece est piece dans estPassage
#demander si une piece peut avoir un num == 0

