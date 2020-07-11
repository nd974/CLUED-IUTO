# -*- coding: utf-8 -*-
"""
						   Projet CLUED'IUTO 
		Projet Python 2018 de 1ere année DUT Informatique Orléans
		
   Module plateau.py
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu c'est à dire l'endroit où les joueurs
   vont se déplacer. Le plateau sera implémenté à partir d'une matrice de case et va gérer une liste de pièces
"""

import matrice
import case
import piece
import entree
import ansiColor

MATRICE_CASES = 'matrice_cases'
LISTE_PIECES = 'liste_pieces'
CASE_VIDE = case.Case(None, None)
COULOIR_LIBRE = case.Case(case.COULOIR, None)

#-----------------------------------------
# contructeur 
#-----------------------------------------

def Plateau(nbLig,nbCol):
	"""
	créer un plateau de nbLig sur nbCol cases vides avec une liste de pièces vide
	paramètres: nbLig et nbCol deux entiers strictement positifs
	"""
	plateau = {
		MATRICE_CASES : matrice.Matrice(nbLig, nbCol, COULOIR_LIBRE),
		LISTE_PIECES : {}
	}
	return plateau

#-----------------------------------------
# accesseurs 
#-----------------------------------------

# plateau de test pour les accesseurs

# Fonctions

def getNbLignesP(plateau):
	"""
	retourne le nombre de lignes du plateau
	paramètre: plateau le plateau considéré
	"""
	return matrice.getNbLignes(plateau[MATRICE_CASES])


def getNbColonnesP(plateau):
	"""
	retourne le nombre de colonnes du plateau
	paramètre: plateau le plateau considéré
	"""
	return matrice.getNbColonnes(plateau[MATRICE_CASES])


def getCase(plateau,ligne,colonne):
	"""
	retourne la case se trouve en (ligne,colonne) dans le plateau
	paramètres: plateau le plateau considéré
				ligne le numéro de la ligne (en commençant par 0)
				colonne le numéro de la colonne (en commençant par 0)
	"""
	return matrice.getVal(plateau[MATRICE_CASES],ligne,colonne)


def getPieces(plateau):
	"""
	retourne la liste des pièces d'un plateau
	paramètre: plateau le plateau considéré
	"""
	return plateau[LISTE_PIECES]


def getCategorieP(plateau,ligne,colonne):
	"""
	retourne la catégorie de la case qui se trouve en (ligne,colonne) dans le plateau
	paramètres: plateau le plateau considéré
				ligne le numéro de la ligne (en commençant par 0)
				colonne le numéro de la colonne (en commençant par 0)
	"""
	la_case = getCase(plateau,ligne,colonne)
	return case.getCategorie(la_case)


def getContenuP(plateau,ligne,colonne):
	"""
	retourne le contenu de la case qui se trouve en (ligne,colonne) dans le plateau
	paramètres: plateau le plateau considéré
				ligne le numéro de la ligne (en commençant par 0)
				colonne le numéro de la colonne (en commençant par 0)
	"""
	la_case = getCase(plateau,ligne,colonne)
	if la_case == None:
		return None
	return case.getContenu(la_case)


def getPassageSecret(plateau,ligne,colonne):
	"""
	retourne le numéro de la pièce accessible via un passage secret si on est en position ligne,colonne.
	retourne None s'il n'y a pas de passage secret
	paramètres: plateau le plateau considéré
				ligne la ligne de la case
				colonne la colonne de la case
	cette fonction retourne None ou un numéro de pièce
	"""
	liste_pieces = getPieces(plateau)
	id_piece = getCategorieP(plateau,ligne,colonne)
	if id_piece and id_piece>0:
		la_piece = liste_pieces[id_piece]
		passage = piece.estPassage(la_piece,ligne,colonne)
		if passage:
			return passage



#-------------------------
# setters et modificateurs
#-------------------------


def setCase(plateau,ligne,colonne,categorie):
	"""
	met une case de type categorie en (ligne,colonne) du plateau (cette case ne contiendra pas de pion)
	paramètres: plateau le plateau considéré 
				ligne le numéro de la ligne (en commençant par 0)
				colonne le numéro de la colonne (en commençant par 0)
				categorie le type de case souhaitée pour cette position
	cette fonction ne retourne rien mais modifie le plateau
	"""
	la_case = case.Case(categorie, None)
	matrice.setVal(plateau[MATRICE_CASES], ligne, colonne, la_case)


def setPieces(plateau,lesPieces):
	"""
	affecte une liste de pièce à un plateau
	paramètres: plateau le plateau considéré
				lesPieces la liste des pièces 
	cette fonction ne retourne rien mais modifie le plateau
	"""
	plateau[LISTE_PIECES] = lesPieces


def enleverPion(plateau,ligne,colonne):
	"""
	enlève le pion qui se trouve sur la case considérée du plateau et retourne ce pion
	paramètres: plateau le plateau considéré
				ligne le numéro de la ligne (en commençant par 0)
				colonne le numéro de la colonne (en commençant par 0
	résultat: un entier indiquant pion qui se trouvait sur la case
	"""

	pion = getContenuP(plateau, ligne, colonne)
	la_case = getCase(plateau, ligne, colonne)
	case.setContenu(la_case, None)
	return pion


def mettrePion(plateau,ligne,colonne,pion):
	"""
	met un pion sur la case se trouvant en (ligne,colonne) du plateau. Si case contenait un pion celui-ci sera écrasé
	paramètres: plateau le plateau considéré
				ligne le numéro de la ligne (en commençant par 0)
				colonne le numéro de la colonne (en commençant par 0)
				pion un entier représentant le pion à mettre
	cette fonction ne retourne rien mais modifie le plateau
	"""
	categorie = getCategorieP(plateau,ligne,colonne)
	setCase(plateau,ligne,colonne,categorie)
	la_case = getCase(plateau, ligne, colonne)
	case.setContenu(la_case, pion)


def poserPionCaseDepart(plateau,listeNumJoueur):
	"""
	Positionne les pions des joueurs sur leur case départ.
	paramètres: plateau le plateau considéré
				listeNumJoueur la liste des numeros des joueurs participant à la partie
	cette fonction ne retourne rien mais modifie le plateau
	"""
	nbLignesP = getNbLignesP(plateau)
	nbColonnesP = getNbColonnesP(plateau)
	for ligne in range(nbLignesP):
		for colonne in range(nbColonnesP):
			categorie_case = getCategorieP(plateau, ligne, colonne)
			if categorie_case:
				if categorie_case < 0 and abs(categorie_case) in listeNumJoueur:
					mettrePion(plateau, ligne, colonne, abs(categorie_case))
				else:
					enleverPion(plateau, ligne, colonne)
	

def posJoueur(plateau,numJoueur):
	"""
	retourne la position du joueur qui porte le numéro numJoueur sous la forme d'un couple(lig,col)
	paramètres: plateau le plateau considéré
				numJoueur un entier strictement positif
	résultat: un couple (lig,col) donnant la position du joueur numJoueur sur le plateau ou 
			  None si le joueur n'est pas sur le plateau
	"""
	nbLignesP = getNbLignesP(plateau)
	nbColonnesP = getNbColonnesP(plateau)
	for ligne in range(nbLignesP):
		for colonne in range(nbColonnesP):
			contenu_case = getContenuP(plateau, ligne, colonne)
			if contenu_case == numJoueur:
				return (ligne,colonne)


def estEntreePiece(plateau,ligne,colonne):
	"""
	Permet de savoir si une case est l'entrée d'une pièce ou non.
	paramètres: plateau le plateau considéré
				ligne la ligne de la case
				colonne la colonne de la case
	cette fonction retourne un booléen
	"""
	for id_piece, une_piece in getPieces(plateau).items():
		if piece.estEntree(une_piece, ligne, colonne):
			return True
	return False


def estPassageSecret(plateau,ligne,colonne):
	"""
	Permet de savoir si une case est un passage secret ou non.
	paramètres: plateau le plateau considéré
				ligne la ligne de la case
				colonne la colonne de la case
	cette fonction retourne un booléen
	"""
	passage_secret = getPassageSecret(plateau, ligne, colonne)
	if passage_secret > 0 :
		return True


def passageNord(plateau,ligne,colonne):
	"""
	teste si on peut passer de la case  à la case adjacente vers le nord
	paramètres: plateau le plateau considéré
				ligne le numéro de la ligne (en commençant par 0)
				colonne le numéro de la colonne (en commençant par 0)
	résultat: un booléen indiquant si le passage est possible ou non
	"""
	if ligne > 0:
		num_pieceA = getCategorieP(plateau,ligne,colonne)
		pieceA = piece.Piece(0)
		if num_pieceA!=None:
			if num_pieceA > 0:
				liste_pieces = getPieces(plateau)
				pieceA = liste_pieces[num_pieceA]
			if num_pieceA == case.COULOIR or num_pieceA < 0 or (entree.NORD, ligne, colonne) in piece.getEntreesDirection(pieceA, entree.NORD):
				num_pieceN = getCategorieP(plateau, ligne-1, colonne)
				pieceN = piece.Piece(0)
				if num_pieceN!=None:
					if num_pieceN > 0:
						liste_pieces = getPieces(plateau)
						pieceN = liste_pieces[num_pieceN]
					if num_pieceN == case.COULOIR or num_pieceN < 0 or (entree.SUD, ligne-1, colonne) in piece.getEntreesDirection(pieceN, entree.SUD):
						return True
	return False


def passageSud(plateau,ligne,colonne):
	"""
	teste si on peut passer de la case  à la case adjacente vers le sud
	paramètres: plateau le plateau considéré
				ligne le numéro de la ligne (en commençant par 0)
				colonne le numéro de la colonne (en commençant par 0)
	résultat: un booléen indiquant si le passage est possible ou non
	"""
	if ligne < getNbLignesP(plateau)-1:
		num_pieceA = getCategorieP(plateau,ligne,colonne)
		pieceA = piece.Piece(0)
		if num_pieceA!=None:
			if num_pieceA > 0:
				liste_pieces = getPieces(plateau)
				pieceA = liste_pieces[num_pieceA]
			if num_pieceA == case.COULOIR or num_pieceA < 0 or (entree.SUD, ligne, colonne) in piece.getEntreesDirection(pieceA, entree.SUD):
				num_pieceS = getCategorieP(plateau, ligne+1, colonne)
				pieceS = piece.Piece(0)
				if num_pieceS!=None:
					if num_pieceS > 0:
						liste_pieces = getPieces(plateau)
						pieceS = liste_pieces[num_pieceS]
					if num_pieceS == case.COULOIR or num_pieceS < 0 or (entree.NORD, ligne+1, colonne) in piece.getEntreesDirection(pieceS, entree.NORD):
						return True
	return False


def passageEst(plateau,ligne,colonne):
	"""
	teste si on peut passer de la case  à la case adjacente vers l'est
	paramètres: plateau le plateau considéré
				ligne le numéro de la ligne (en commençant par 0)
				colonne le numéro de la colonne (en commençant par 0)
	résultat: un booléen indiquant si le passage est possible ou non
	"""
	if colonne < getNbColonnesP(plateau)-1:
		num_pieceA = getCategorieP(plateau,ligne,colonne)
		pieceA = piece.Piece(0)
		if num_pieceA!=None:
			if num_pieceA > 0:
				liste_pieces = getPieces(plateau)
				pieceA = liste_pieces[num_pieceA]
			if num_pieceA == case.COULOIR or num_pieceA < 0 or (entree.EST, ligne, colonne) in piece.getEntreesDirection(pieceA, entree.EST):
				num_pieceE = getCategorieP(plateau, ligne, colonne+1)
				pieceE = piece.Piece(0)
				if num_pieceE!=None:
					if num_pieceE > 0:
						liste_pieces = getPieces(plateau)
						pieceE = liste_pieces[num_pieceE]
					if num_pieceE == case.COULOIR or num_pieceE < 0 or (entree.OUEST, ligne, colonne+1) in piece.getEntreesDirection(pieceE, entree.OUEST):
						return True
	return False


def passageOuest(plateau,ligne,colonne):
	"""
	teste si on peut passer de la case  à la case adjacente vers l'ouest
	paramètres: plateau le plateau considéré
				ligne le numéro de la ligne (en commençant par 0)
				colonne le numéro de la colonne (en commençant par 0)
	résultat: un booléen indiquant si le passage est possible ou non
	"""
	if colonne > 0:
		num_pieceA = getCategorieP(plateau,ligne,colonne)
		pieceA = piece.Piece(0)
		if num_pieceA!=None:
			if num_pieceA > 0:
				liste_pieces = getPieces(plateau)
				pieceA = liste_pieces[num_pieceA]
			if num_pieceA == case.COULOIR or num_pieceA < 0 or (entree.OUEST, ligne, colonne) in piece.getEntreesDirection(pieceA, entree.OUEST):
				num_pieceO = getCategorieP(plateau, ligne, colonne-1)
				pieceO = piece.Piece(0)
				if num_pieceO!=None:
					if num_pieceO > 0:
						liste_pieces = getPieces(plateau)
						pieceO = liste_pieces[num_pieceO]
					if num_pieceO == case.COULOIR or num_pieceO < 0 or (entree.EST, ligne, colonne-1) in piece.getEntreesDirection(pieceO, entree.EST):
						return True
	return False


def marquageDirect(plateau,calque,ancienneVal,nouvelleVal):
	"""
	permet de marquer avec nouvelleVal les cases non marquées
	adjacentes à une case marquée par ancienneVal
	paramètres: plateau le plateau considéré
				calque une matrice de la même dimension que le plateau et qui porte le marquage
				ancienneVal la valeur de marquage recherchée
				nouvelleVal la valeur utilisée pour marquer les nouvelle case
	cette fonction ne retourne rien mais modifie le claque
	"""
	nbLignes = getNbLignesP(plateau)
	nbColonnes = getNbColonnesP(plateau)
	modif=False
	for ligne in range(nbLignes):
		for colonne in range(nbColonnes):
			if matrice.getVal(calque, ligne, colonne) == None:
				v_Nord = None
				v_Est = None
				v_Sud = None
				v_Ouest = None
				if passageNord(plateau, ligne, colonne):
					v_Nord = matrice.getVal(calque, ligne-1, colonne)
					if v_Nord:
						v_Nord = v_Nord %2
				if passageSud(plateau, ligne, colonne):
					v_Sud = matrice.getVal(calque, ligne +1, colonne)
					if v_Sud:
						v_Sud = v_Sud %2
				if passageEst(plateau, ligne, colonne):
					v_Est = matrice.getVal(calque, ligne, colonne +1)
					if v_Est:
						v_Est = v_Est %2
				if passageOuest(plateau, ligne, colonne):
					v_Ouest = matrice.getVal(calque, ligne, colonne -1)
					if v_Ouest:
						v_Ouest = v_Ouest %2

				ens_voisins = {v_Nord, v_Est, v_Ouest, v_Sud}

				if ancienneVal%2 in ens_voisins:
					matrice.setVal(calque, ligne, colonne, nouvelleVal)
					modif=True		
	return modif


def casesAccessibles(plateau,listeDepart,distance):
	"""
	retourne la liste des cases accessibles sous la forme de liste de couples 
	de coordonnées (lig,col)
	paramètres: plateau le plateau considéré
				listeDepart: une liste de couples (lig,col) indiquant les points de départ de la recherche
				distance: un entier positif indiquant de combien de cases on a le droit de se déplacer
	résultat: la liste des case atteignable à partir d'un des départs en utilisant moins de distance déplacements
	"""
	res = set()
	nbLignes = getNbLignesP(plateau)
	nbColonnes = getNbColonnesP(plateau)
	for (lig,col) in listeDepart:
		calque = matrice.Matrice(nbLignes, nbColonnes, None)
		matrice.setVal(calque, lig, col, 0)
		for dist in range(0,distance):
			marquageDirect(plateau, calque, dist, dist+1)
		for ligne in range(nbLignes):
			for colonne in range(nbColonnes):
				dist2 = matrice.getVal(calque,ligne,colonne)
				if dist2:
					if not getContenuP(plateau, ligne, colonne):
						if getCategorieP(plateau, ligne, colonne) and getCategorieP(plateau, ligne, colonne) > 0:
							res.add((ligne, colonne))
						elif dist2%2==distance%2:
							res.add((ligne, colonne))
	return res


def distancePieces(plateau,lig,col):
	"""
	retourne un dictionnaire dont les clés sont les identifiant des pièces et les valeurs la distance
	a parcourir pour atteindre la pièce à partir de la case de coordonnées (lig,col)
	paramètres: plateau le plateau considéré
				lig: le numéro de la ligne de la case considérée
				col: le numéro de la colonne de la case considérée
	résultat: le dictionnaire décrit plus haut
	"""
	dico_idpiece_distance = {}
	nbLignes = getNbLignesP(plateau)
	nbColonnes = getNbColonnesP(plateau)
	calque = matrice.Matrice(nbLignes, nbColonnes, None)
	matrice.setVal(calque, lig, col, 0)
	modif = True
	i=0

	while modif:
		modif = marquageDirect(plateau, calque, i, i+1)
		i += 1

	def chercherLaDistance(une_entree):
		ligne_une_entree, colonne_une_entree = entree.getLigne(une_entree), entree.getColonne(une_entree)
		return matrice.getVal(calque, ligne_une_entree, colonne_une_entree)

	for id_piece, instance_piece in getPieces(plateau).items():
		dico_idpiece_distance[id_piece] = chercherLaDistance(min(piece.getListeEntrees(instance_piece), key = chercherLaDistance))
	return dico_idpiece_distance


def accessiblesJoueur(plateau,numJoueur,distance):
	"""
	retourne une liste de couple (lig,col) indiquant les cases accessibles pour le joueur numJoueur
	à la distance
	paramètres: plateau le plateau considéré
				numJoueur un entier strictement positif
				distance  un entier strictement positif indiquant la distance maximale
	résultat: la liste des positions accessible par le joueur
	"""
	position_joueur = posJoueur(plateau, numJoueur)
	accessibles_joueur = casesAccessibles(plateau, [position_joueur], distance)
	return accessibles_joueur


# ----------------------------------------------------
# chargement d'un plateau à partir d'un fichier texte
# et affichage en mode texte d'un plateau
# ----------------------------------------------------

def traiterCase(laCase,lig,col,plateau,pieces):
	if laCase=='':
		setCase(plateau,lig,col,None)
	else:
		contenu=laCase.split(";")
		sorte=int(contenu[0])
		setCase(plateau,lig,col,sorte)
		if sorte>0 and sorte not in pieces:
			pieces[sorte]=piece.Piece(sorte)
		if len(contenu)>1:
			if contenu[1]=='P':
				piece.setPassage(pieces[sorte],int(contenu[2]),lig,col)
			elif contenu[1]=='N':
				piece.addEntree(pieces[sorte],entree.Entree(entree.NORD,lig,col))
			elif contenu[1]=='E':
				piece.addEntree(pieces[sorte],entree.Entree(entree.EST,lig,col))
			elif contenu[1]=='S':
				piece.addEntree(pieces[sorte],entree.Entree(entree.SUD,lig,col))
			elif contenu[1]=='O':
				piece.addEntree(pieces[sorte],entree.Entree(entree.OUEST,lig,col))
			elif contenu[1]=='J':
				if sorte>1:
					piece.addJoueur(pieces[sorte],int(contenu[2]))
				else:
					mettrePion(plateau,lig,col,int(contenu[2]))
				
def lirePlateau(nomFichier):
	texte=""
	try:
		fic=open(nomFichier)
		texte=fic.read()
		fic.close()
	except:
		print("probleme de lecture du fichier")
		return None
	lignes=texte.split("\n")
	nbLignes=len(lignes)
	if nbLignes==0:
		return None
	
	nbColonnes=len(lignes[0].split(","))
	plateau=Plateau(nbLignes-1,nbColonnes)
	lig=0
	lesPieces={}
	for ligne in lignes[:-1]:
		cases=ligne.split(",")
		col=0
		for c in cases:
			traiterCase(c,lig,col,plateau,lesPieces)
			col+=1
		lig+=1
	setPieces(plateau,lesPieces)
	return plateau



def afficherPlateau(plateau,information=[],decalage=8,debutInfo=3):# TODO enlever +str((lig,col))+'||'
	joueurPiece={}
	pieceIdentifiees={}
	sortePrec=0
	for lig in range(getNbLignesP(plateau)):
		print(' '*decalage,sep='',end='')
		for col in range(getNbColonnesP(plateau)):
			c=getCase(plateau,lig,col)
			sorte=case.getCategorie(c)
			if sorte==None:
				print(' ',sep='',end='')
			elif sorte<=0:
				couleurF=ansiColor.GRIS+60
				pion=case.getContenu(c)
				if pion==None:
					if sorte<0:
						car='X'			
						couleurT=-sorte
					else:
						car=' '			
						couleurT=ansiColor.NORMAL
				else:
					car='@'			
					couleurT=pion+ansiColor.CLAIR
				ansiColor.pcouleur(car,couleurT,couleurF,ansiColor.GRAS)
			else:
				if sorte not in pieceIdentifiees:
					pieceIdentifiees[sorte]=[1,1]
				elif sorte==sortePrec:
					pieceIdentifiees[sorte][1]+=1
				else:
					pieceIdentifiees[sorte][0]+=1
					pieceIdentifiees[sorte][1]=1               
				couleurF=sorte%7+sorte//7
				couleurT=ansiColor.NORMAL
				if piece.estEntree(getPieces(plateau)[sorte],lig,col):
					car='/'				
				else:
					dest=piece.estPassage(getPieces(plateau)[sorte],lig,col)
					if dest!=0:
						car='P'			
						couleurT=dest%7+dest//7
					else:
						if sorte not in joueurPiece:
							joueurPiece[sorte]=0
						listeJoueur=piece.getContenu(getPieces(plateau)[sorte])
						if joueurPiece[sorte]<len(listeJoueur):
							couleurT=listeJoueur[joueurPiece[sorte]]+ansiColor.CLAIR
							car='@'				
							joueurPiece[sorte]+=1
						else:
							if pieceIdentifiees[sorte]==[3,3]:
								car=str(sorte%10)   
							else:
								car=' '                
							couleurT=ansiColor.NORMAL
				ansiColor.pcouleur(car,couleurT,couleurF)
			sortePrec=sorte
		if lig>=debutInfo and lig<debutInfo+len(information):
			print('  ',information[lig-debutInfo])
		else:
			print()


# +str((lig,col))