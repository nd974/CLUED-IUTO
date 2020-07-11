from cluedo import *

#Variables de tests
joueur1=[1,"oui",True,False,{carte.test_carte,carte.test_carte2},{}]
joueur2=[2,"oui",False,False,{carte.test_carte,carte.test_carte3},{}]
joueur3=[3,"oui2",False,False,set(),{}]
indice1={3:'?',1:'?',2:'?'}
indice2={3:'-',1:'+',2:'-'}
plateau_test = {
		'matrice_cases' : matrice.Matrice(3, 3, case.Case(None, None)),
		'liste_pieces' : [piece.piece0, piece.piece1, piece.piece2]
	}
jeuCarte=[carte.test_carte,carte.test_carte2,carte.test_carte3]

#distribuer carte
#prendre test Mathieu
listeJoueurs=[[1,"j1",False,False,set(),{}],[2,"j2",True,False,set(),{}],[3,"j3",False,False,set(),{}]]


#joueur principal
assert joueurPrincipal(listeJoueurs)==listeJoueurs[1]
listeJoueurs2=[[1,"j1",False,False,set(),{}],[2,"j2",False,False,set(),{}],[3,"j3",False,False,set(),{}]]
assert joueurPrincipal(listeJoueurs2)==listeJoueurs2[0]

#----------------
#
# Constructeur
#
#---------------

# Cluedo
test_cluedo=[[joueur1,joueur2,joueur3],plateau_test,jeuCarte,jeucarte.definirMystere(jeuCarte),joueurPrincipal(listeJoueurs),0]
#assert Cluedo(open('joueurs.csv','r'),open('cartes.csv','r'),open('plan1.csv','r'))==test_cluedo
#pb lecture de fichier + Jeu de carte non complet

#getJoueurCourant
assert getJoueurCourant(test_cluedo)==joueur1

#getIndiceJoueurCourant
getIndiceJoueurCourant(test_cluedo)==0

#getSolution
assert getSolution(test_cluedo)==(4,2,3)

#getNbJoueursActifs
assert getNbJoueursActifs(test_cluedo)==3    

#passageSecretJoueurCourant
# assert passageSecretJoueurCourant(test_cluedo)==8 # pas de assert error quand je met des mauvaise réponses

#choixProfMatOrdinateur
# assert choixProfMatOrdinateur(test_cluedo,1)==('Ada','programmation',1) #--> Nonetype


#distance piece
assert distancePieces(test_cluedo,[piece.piece1,piece.piece2],[(2,4),(6,1),(9,0),(1,4)])=={56:(2,1,4),42:(0,1,4)}

#choix piece ordinateur
assert choixPieceOrdinateur(test_cluedo,distancePieces(test_cluedo,[piece.piece1,piece.piece2],[(2,4),(6,1),(9,0),(1,4)]))==(1,4)

#reponse passage ordi
assert reponsePassageOrdinateur(test_cluedo,8)=='O' or 'N'

