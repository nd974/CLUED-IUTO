# -*- coding: utf-8 -*-
"""
						   Projet CLUED'IUTO 
		Projet Python 2018 de 1ere année DUT Informatique Orléans
		
   Module cluedo.py
   ~~~~~~~~~~~~~~~~
   
   Ce module gère le jeu du cluedo. 
"""

import joueur
import plateau
import jeucarte
import carte
import ficheIndices
import mystere
import piece
import random
import matrice
import case


def distribuerCartes(jeuCarte,listeJoueurs):
	"""
	distribue les carte d'un jeu de carte aux joueurs
	paramètres jeuCarte un jeu de carte mélangé
			   listeJoueurs la liste des joueurs participant au jeu
	"""
	i=0
	y=0
	while i<len(jeuCarte):
		if carte.estDistribuable(jeuCarte[i]):
			if y==len(listeJoueurs):
				y=0
			joueur.ajouterCarte(listeJoueurs[y],jeuCarte[i])
			y+=1
		i+=1
			


def joueurPrincipal(listeJoueurs):
	"""
	retourne le joueur principal c'est à dire le premier joueur humain
	ou si aucun joueur est humain, c'est le premier joueur
	paramètre: listeJoueurs la liste des joueurs participant au jeu
	résultat le joueur principal
	"""
	if listeJoueurs==[]:
		return None
	for joueurs in listeJoueurs:
		if joueur.estHumain(joueurs):
			return joueurs
	return listeJoueurs[0]


#-----------------------------------------
# contructeur
#-----------------------------------------
def Cluedo(ficJoueurs,ficCartes,ficPlateau):
	"""
	Construit un nouveau jeu de cluedo à partir de trois fichiers: les joueurs, les cartes et le plateau
	paramètres: ficJoueurs le nom du fichier des joueurs
				ficCartes le nom du fichier contenant la description des cartes
				ficPlateau le nom du fichier contenant l'état du plateau
	Cette fonction retourne un nouveau jeu de cluedo (une nouvelle partie), elle va donc initialiser les joueurs,
	le plateau le jeu de carte, tirer au hasard une énigme et distribuer les cartes au joueurs. 
	Les fiches indices de chaque joueur seront initialisées et les pions des joueurs seront placés sur leur départ
	Le joueur principal (celui dont on voit la fiche indice) est soit le joueur humain s'il y en a un, le premier joueur sinon
	"""
	jeuCarte=jeucarte.lireJeuCarte(ficCartes)
	jeucarte.melangerJeu(jeuCarte)
	listeJoueurs=joueur.lireJoueurs(ficJoueurs)
	myst=jeucarte.definirMystere(jeuCarte)
	distribuerCartes(jeuCarte,listeJoueurs)
	plato=plateau.lirePlateau(ficPlateau)
	liste_num_joueur=[]
	for joueurs in listeJoueurs:
		liste_num_joueur.append(joueur.getNum(joueurs))
		fiche_joueur=ficheIndices.FicheIndices(listeJoueurs,jeuCarte)
		ficheIndices.initFicheIndices(fiche_joueur,joueur.getNum(joueurs),joueur.getCartes(joueurs))
		joueurs[5]=fiche_joueur
	plateau.poserPionCaseDepart(plato,liste_num_joueur)
	return [listeJoueurs,plato,jeuCarte,myst,joueurPrincipal(listeJoueurs),1]


def getJoueurCourant(cluedo):
	"""
	retourne le joueur courant (c-à-d celui à qui c'est le tour de jouer)
	paramètre: cluedo le jeu de cluedo
	resultat: le joueur 
	"""
	try:
		return cluedo[0][0]
	except:
		return None

def getIndiceJoueurCourant(cluedo):
	"""
	retourne l'indice dans l'ordre des joueurs du joueur courant (c-à-d celui à qui c'est le tour de jouer)
	paramètre: cluedo le jeu de cluedo
	resultat: un entier représentant le numéro d'ordre du joueur
	"""
	return 0 

def getSolution(cluedo):
	"""
	retourne la solution à trouver sous la forme d'un Mystere
	paramètre: cluedo le jeu de cluedo
	resultat: une structure de type Mystere solution de l'énigme
	"""
	return cluedo[3]

def getNbJoueurs(cluedo):
	"""
	retourne le nombre de joueurs engagés dans la partie (éliminés ou non)
	paramètre: cluedo le jeu de cluedo
	"""
	return len(cluedo[0])

def getNbJoueursActifs(cluedo):
	"""
	retourne le nombre de joueurs engagés dans la partie qui ne sont pas éliminés
	paramètre: cluedo le jeu de cluedo
	"""
	cpt=0
	for joueurs in cluedo[0]:
		if not joueur.estElimine(joueurs):
			cpt+=1
	return cpt

def getJoueurPrincipal(cluedo):
	"""
	retourne le joueur principal (c-à-d celui dont on voit le jeu)
	paramètre: cluedo le jeu de cluedo
	resultat: le joueur 
	"""
	return cluedo[4]
	
def getNumTour(cluedo):
	"""
	retourne le numéro du tour actuel
	paramètre: cluedo le jeu de cluedo
	resultat: le numéro du tour actuel 
	"""
	return cluedo[5]

def getPlateau(cluedo):
	"""
	retourne le plateau du cluedo
	paramètre: cluedo le jeu de cluedo
	resultat: le plateau associé au cluedo 
	"""
	return cluedo[1]

def getJeuCartes(cluedo):
	"""
	retourne le jeu de cartes du cluedo
	paramètre: cluedo le jeu de cluedo
	resultat: le jeu de cartes associé au cluedo 
	"""
	return cluedo[2]

def getListeJoueurs(cluedo):
	"""
	retourne la liste des joueurs participant à la partie de cluedo
	paramètre: cluedo le jeu de cluedo
	resultat: la liste des joueurs participant à la partie 
	"""
	return cluedo[0]

def getNumPieceHypothese(cluedo):
	"""
	Retourne le numero de la piece dans laquelle le joueur courant
	formule son hypothese
	"""
	return 10
	
def incNumTour(cluedo):
	"""
	ajoute 1 au numéro de tour et change le joueur courant.
	Attention il faut tenir compte des joueurs éliminés
	paramètre: cluedo le jeu de cluedo
	cette fonction ne retourne rien mais modifie le cluedo
	"""
	cluedo[5]+=1
	temp=getJoueurCourant(cluedo)
	listeJoueurs=getListeJoueurs(cluedo)
	listeJoueurs.remove(temp)
	i=len(listeJoueurs)-1
	while i>0:
		if not joueur.estElimine(listeJoueurs[i]):
			if i==len(listeJoueurs)-1:
				listeJoueurs.append(temp)
			else:
				listeJoueurs.insert(i+1,temp)
			break
		i-=1

def elimineJoueurCourant(cluedo):
	"""
	elimine le joueur courant
	paramètre: cluedo le jeu de cluedo
	cette fonction ne retourne rien mais modifie le cluedo
	"""
	joueur_courant=getJoueurCourant(cluedo)
	joueur.setElimine(joueur_courant,True)

	
def distancePieces(cluedo,listePieces,listeDest):
	"""
	retourne sous la forme d'un dictionnaire la case la plus proche de chacune des pièces
	paramètres: cluedo le jeu de cluedo
				listesPieces la liste des pièces du jeu
				listeDest une liste de coordonnées de case données sous la forme (lig,col)
	resultat: un dictionnaire dont les clés sont les numéros de pièce et les valeurs un triplé 
			  (dist,lig,col) indiquant la case la plus proche de la pièce a les coordonnée lig,col
			  qui se situe à une distance dist de la pièce
	"""
	le_plateau = getPlateau(cluedo)
	dico_distance_piece = {}
	for (lig, col) in listeDest:
		dico_dest = plateau.distancePieces(le_plateau, lig, col)
		for id_piece, distance in dico_dest.items():
			if id_piece not in dico_distance_piece:
				dico_distance_piece[id_piece] = (distance, lig, col)
			if distance < dico_distance_piece[id_piece][0]:
				dico_distance_piece[id_piece] = (distance, lig, col)
	return dico_distance_piece


def choixPieceOrdinateur(cluedo,distances):
	"""
	retourne les coordonnées de la case choisie par le joueur ordinateur parmi une liste de destinations possibles
	paramètres: cluedo le jeu de cluedo
				distances un dictionnaire résultat de la fonction distancePieces
						  les clés sont les numéros des pièces et les valeur un triplet (dist,lig,col)
	résultat les coordonnées de la case choisie sous la forme (lig,col)
	"""
	def distance_separant(num_piece):
		if num_piece!=getNumPieceHypothese:
			return distances[num_piece][0]
		solution=ficheIndices.hypothesesSures(joueur.getFiche(getJoueurCourant(cluedo)))
		if 1 in solution.keys() and 2 in solution.keys() and 3 in solution.keys():
			return 0
		return 9999 #ne pas aller dans cette salle si on n'a pas la solution
	num_piece_dist_min=min(distances.keys(),key=distance_separant)
	return (distances[num_piece_dist_min][1],distances[num_piece_dist_min][2])

def reponsePassageOrdinateur(cluedo,numP):
	"""
	retourne la réponse d'un joueur ordinateur à la question souhaitez vous prendre le passage secret
	cette fonction peut être complètement aléatoire ou tenir compte d'une stratégie (voir les fonctions
	de la structure ficheIndices
	paramètres: cluedo le jeu de cluedo
			   numP le numéro de la pièce destination
	résultat: 'O' ou 'N'
	"""
	reponse=random.randint(1,2)
	if reponse==1:
		return 'O'
	return 'N'

def passageSecretJoueurCourant(cluedo):
	"""
	retourne soit None si le joueur courant ne se trouve pas dans une pièce où il y a un passage secret
	soit un triplet numPieceDest,lig,col indiquant le numéro de la pièce destination du passage
	la postion du passage dans la pièce où se trouve le joueur courant
	paramètre: cluedo le jeu de cluedo
	"""
	plato=getPlateau(cluedo)
	(pos_x,pos_y)=plateau.posJoueur(plato,joueur.getNum(getJoueurCourant(cluedo)))
	liste_pieces=plateau.getPieces(plato)
	num_piece= case.getCategorie(plateau.getCase(plato,pos_x,pos_y))
	for num_piece_actuel,une_piece in liste_pieces.items():
		if num_piece_actuel==num_piece:
			if piece.getPassage(une_piece)!=None:
				return (piece.getPassage(une_piece),pos_x,pos_y)


def choixProfMatOrdinateur(cluedo,numPiece):
	"""
	retourne sous la forme d'un couple numProf,numMat le choix du joueur courant géré par un ordinateur
	cette fonction se sert la fonction creerUneHypothese de la structure ficheIndices
	paramètres: cluedo le jeu de cluedo
				numPiece le numéro de la pièce où se trouve le joueur courant
	résultat un couple numProf,numMat
	"""
	joueur_courant=getJoueurCourant(cluedo)
	choix=ficheIndices.creerUneHypothese(joueur.getFiche(joueur_courant),joueur.getNum(joueur_courant),numPiece)
	return choix[0],choix[1]

def choixSolutionOrdinateur(cluedo):
	"""
	retourne sous la forme d'une structure Mystere la solution proposée par le joueur courant géré par un ordinateur
	cette fonction se sert la fonction hypothesesSures de la structure ficheIndices
	paramètre: cluedo le jeu de cluedo
	résultat un mystere
	"""
	hypo_sures=ficheIndices.hypothesesSures(joueur.getFiche(getJoueurCourant(cluedo)))
	return (carte.getNum(hypo_sures[1]),carte.getNum(hypo_sures[2]),carte.getNum(hypo_sures[3]))

def demanderJoueurOrdinateur(cluedo,joueurInterroge,hypothese):
	"""
	donne la réponse d'un joueur géré par l'ordinateur à une hypothèse proposée par le joueur courant
	cette fonction utilise la fonction reponseHypothese de joueur
	paramètres: cluedo          : le jeu de cluedo
				joueurInterroge : le joueur interrogé
				hypothese       : l'hypothèse formée par le joueur courant sous la forme d'une structure mystere
	résulat: None si le joueur interrogé ne possède aucune carte, sinon une des cartes que le joueur interrogé possède
	"""
	return joueur.reponseHypothese(joueurInterroge,hypothese)
	
def jouerDe(cluedo):
	"""
	lance les dés (c-à-d choisit aléatoirement un entier compris entre 2 et 12) puis calcule pour chaque pièce
	la distance à laquelle le joueur courant peut s'approcher en fonction des points obtenus sur les dés
	paramètres: cluedo          : le jeu de cluedo
	résultat: un dictionnaire dont les clés sont les numéros de pièce et les valeurs la
			  distance à laquelle le joueur peut s'approcher 
			  de la pièce grâce aux points obtenus aux dés (voir fonction distancePieces)
	"""
	des1=random.randint(1,6)
	des2=random.randint(1,6)
	des=des1+des2
	plato=getPlateau(cluedo)
	numJoueur=joueur.getNum(getJoueurCourant(cluedo))
	(pos_x_joueur,pos_y_joueur)=plateau.posJoueur(plato,numJoueur)
	liste_case_accessibles=plateau.accessiblesJoueur(plato,numJoueur,des)
	listePieces=plateau.getPieces(plato)
	dico_dist_piece=distancePieces(cluedo,listePieces,liste_case_accessibles)
	return des,dico_dist_piece  


def deplacerJoueurCourant(cluedo,lig,col):
	"""
	cette fonction modifie le plateau du cluedo en enlevant le pion du joueur courant de son emplacement actuel
	et le positionnant sur la case destination. Elle retourne de plus la catégorie de la case destination
	paramètres: cluedo          : le jeu de cluedo
				lig: le numéro de la ligne destination
				col: le numéro de la colonng destination
	resultat: catégorie de la case destination (numero de la pièce ou couloir)
	"""
	plato=getPlateau(cluedo)
	joueurs=getJoueurCourant(cluedo)
	(pos_x_joueur,pos_y_joueur)=plateau.posJoueur(plato,joueur.getNum(joueurs))
	plateau.enleverPion(plato,pos_x_joueur,pos_y_joueur)
	plateau.mettrePion(plato,lig,col,joueur.getNum(joueurs))
	categorie=case.getCategorie(plateau.getCase(plato,lig,col))
	return categorie
	
# ---------------------------------------------
# Fonction d'affichage
# ---------------------------------------------
def afficherCluedo(cluedo,information):
	"""
	affiche la vue du cluedo c'est-à-dire le plateau ainsi que la fiche indice du joueur principal et le message d'information
	paramètres: cluedo le jeu de cluedo
				information le message à afficher avec le jeu
	"""
	print()
	joueurCourant=getJoueurCourant(cluedo)
	debutInformation="--------- Tours numéro "+str(getNumTour(cluedo))+"\n"+\
		"    c'est au joueur "+str(joueur.getNum(joueurCourant))+" appelé "+joueur.getNom(joueurCourant)+ " de jouer\n"
	
	plateau.afficherPlateau(getPlateau(cluedo),(debutInformation+information).split('\n'))
	print(ficheIndices.string(joueur.getFiche(getJoueurPrincipal(cluedo))))
