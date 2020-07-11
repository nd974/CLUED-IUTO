#! /usr//bin/python3
# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module cluedoTexte.py
   ~~~~~~~~~~~~~~~~
   
   Ce module est le programme principal du cluedo en mode texte. Vous n'avez rien à implmenter dans ce fichier
"""
import cluedo
import jeucarte
import carte
import mystere
import joueur
import ficheIndices
#from tkinter import *
#from tkinter.messagebox import *

def infoDistance(distances):
    """
    construit une chaine de caractères indiquant pour chaque pièce la distance
    à laquelle le joueur peut se retrouver
    paramètres: cluedo le jeu de cluedo    
                distances un dictionnaire résultat de la fonction distancePieces
                          les clés sont les numéros des pièces et les valeur un triplet (dist,lig,col)
    résultat: une chaine de caractères rendant compte du contenu de distances
    """
    piecesAtteintes='Vous pouvez atteindre les pièces:'
    autresPièces='Voici les distances respectives aux pièces suivantes:'
    for numP,(dist,_,_) in distances.items():
        if dist==0:
            piecesAtteintes+=' '+str(numP)
        else:
            autresPièces+=' '+str(numP)+'('+str(dist)+')'
    return piecesAtteintes+'\n'+autresPièces

def traiterCocher(clu,arguments):
    """
    permet au joueur humain de completer sa fiche en plus de ce que l'ordinateur aura automatique mis à jour
    """
    commande=arguments.split()
    if len(commande)<4:
        return -1,"La commande cocher doit contenir la categorie et le numéro de la carte, le numéro du joueur et le type d'info\nPar exemple: 1 4 2 + pour indiquer que l'on pense que le joueur 2 possède la carte 4 de la catégorie PERSONNE"
    if commande[3] not in '+-':
        return -1,"L'indication doit être + (possède) ou - (ne possède pas)"
    if commande[0] not in str(carte.PROFESSEUR)+str(carte.MATIERE)+str(carte.SALLE):
        return -1,"la catégorie de carte doit être "+str(carte.PROFESSEUR)+" "+str(carte.MATIERE)+" "+str(carte.SALLE)
    if not commande[1].isdigit() or int(commande[1]) not in jeucarte.getListeNumCarteCategorie(cluedo.getJeuCartes(cluedo)):
        return -1,"les numéros de carte possibles pour cette catégorie sont "+str(jeucarte.getListeNumCarteCategorie(cluedo.getJeuCartes(cluedo)))
    if  not commande[1].isdigit() or int(commande[1]) not in range(1,getNbJoueurs(cluedo)+1):
        return -1, "les numéros de joueur possibles sont les chiffres entre 1 et "+str(getNbJoueurs(cluedo)+1)
    ficheIndices.connaissance(joueur.getFiche(cluedo.getJoueurCourant(cluedo)),joueur.getNum(cluedo.getJoueurCourant(cluedo)),\
                              int(commande[1]),int(commande[0]),commande[3])
    return 0, "Indication prise en compte"


def choixPieceHumain(distances):
    """
    Interroge l'utilisateur humain sur la pièce qu'il veut atteindre
    paramètres: distances un dictionnaire dont le clé sont les numéro de pièce et les valeurs la position
                où le joueur peut s'approcher au plus prêt de la pièce
    resultat: les coordonnées de la case atteignable par l'utilisateur pour s'approcher au plus prêt de la pièce choisie
              -1,-1 si le joueur a entré une valeur incorrecte.
    """
    try:
        rep=int(input())
    except:
        return -1,-1
    if rep not in distances:
        return -1,-1
    return distances[rep][1],distances[rep][2]

def getDestination(clu, distances, humain):
    if humain:
        return choixPieceHumain(distances)
    else:
        return cluedo.choixPieceOrdinateur(clu,distances)

def choixProfMatHumain(jeuCarte):
    rep=input()
    try:
        prof,mat=rep.split(',')
        prof=int(prof)
        mat=int(mat)
        if prof not in jeucarte.getListeNumCarteCategorie(jeuCarte,carte.PROFESSEUR) or\
           mat  not in jeucarte.getListeNumCarteCategorie(jeuCarte,carte.MATIERE):
            return -1,-1
        return prof,mat
    except:
        return -1,-1

def getHypothese(clu,numPiece,humain):
    if humain:
        prof,mat=choixProfMatHumain(cluedo.getJeuCartes(clu))
    else:
        prof,mat=cluedo.choixProfMatOrdinateur(clu,numPiece)
    if prof ==-1 or mat==-1:
        return None
    return {carte.PROFESSEUR:prof,carte.MATIERE:mat,carte.SALLE:numPiece}

def choixSolutionHumain(jeuCarte):
    rep=input()
    try:
        prof,mat,salle=rep.split(',')
        prof=int(prof)
        mat=int(mat)
        salle=int(salle)
        if prof not in jeucarte.getListeNumCarteCategorie(jeuCarte,carte.PROFESSEUR) or\
           mat  not in jeucarte.getListeNumCarteCategorie(jeuCarte,carte.MATIERE) or\
           salle not in jeucarte.getListeNumCarteCategorie(jeuCarte,carte.SALLE):
            return -1,-1,-1
        return prof,mat,salle
    except:
        return -1,-1

def getLaSolution(clu,humain):
    if humain:
        prof,mat,salle=choixSolutionHumain(cluedo.getJeuCartes(clu))
        if prof!=-1 and mat!=-1 and salle!=-1:
            return mystere.Mystere(prof,mat,salle)
        else:
            return None
    else:
        return cluedo.choixSolutionOrdinateur(clu)


def demanderJoueurHumain(clu,information,joueurInterroge,hp):
    """
    réponse d'un joueur humain à une requête
    """
    possedees=joueur.cartesPossedees(joueurInterroge,hp)
    if possedees==[]:
        cluedo.afficherCluedo(clu,information+"\nVous n'avez aucune carte!\n")
        input()
        return None
    if len(possedees)==1:
        cluedo.afficherCluedo(clu,information+"\nVous ne possédez que la carte "+carte.getNom(possedees[0])+"!\n")
        input()
        return possedees[0]
    infoChoix='\nVous possédez les cartes suivantes:\n'
    for i in range(len(possedees)):
        infoChoix+="   "+str(i+1)+" "+carte.getNom(possedees[i])+"\n"
    infoChoix+='Laquelle montrez vous?\nVeuillez entrez un chiffre entre 1 et '+str(len(possedees))+'\n'
    msgErreur=""
    while True:
        cluedo.afficherCluedo(clu,information+infoChoix+msgErreur)
        rep=input()
        if rep.isdigit():
            rep=int(rep)
            if rep>0 and rep<=len(possedees):
                cluedo.afficherCluedo(clu,information+"Vous avez montré "+carte.getNom(possedees[rep-1])+"\n")
                return possedees[rep-1]
        msgErreur="Réponse incorrecte\n"

def interrogerJoueurs(clu,hypothese):
    joueurCourant=cluedo.getJoueurCourant(clu)
    ficheJoueurCourant=joueur.getFiche(joueurCourant)
    indiceJoueurCourant=cluedo.getIndiceJoueurCourant(clu)
    nbJoueurs=cluedo.getNbJoueurs(clu)
    listeJoueurs=cluedo.getListeJoueurs(clu)
    information=""
    for i in range(1,nbJoueurs):
        indiceInterroge=(indiceJoueurCourant+i)%nbJoueurs
        joueurInterroge=listeJoueurs[indiceInterroge]
        numJoueurInterroge=joueur.getNum(joueurInterroge)
        information+="\nle joueur "+str(numJoueurInterroge)+" est interrogé"
        if joueur.estHumain(joueurInterroge) and joueurInterroge==cluedo.getJoueurPrincipal(clu) and\
           joueur.reponseHypothese(joueurInterroge,hypothese)!=None:
            cluedo.afficherCluedo(clu,information)
            rep=demanderJoueurHumain(clu,information,joueurInterroge,hypothese)
        else:
            rep=cluedo.demanderJoueurOrdinateur(clu,joueurInterroge,hypothese)
        if rep!=None:
            ficheIndices.connaissance(ficheJoueurCourant,numJoueurInterroge,carte.getNum(rep),carte.getCategorie(rep),\
                                      ficheIndices.POSSEDE)
            if joueurCourant==cluedo.getJoueurPrincipal(clu):
                information+="\nLe joueur "+str(numJoueurInterroge)+ " vous a montré "+carte.getNom(rep)
            else:
                information+="\nLe joueur "+str(numJoueurInterroge)+ " a montré une carte"
            break
        else:
            information+="\nLe joueur "+str(numJoueurInterroge)+ " ne possède aucune carte"
            for cat,num in hypothese.items():
                for j in range(nbJoueurs):
                    ficheIndices.connaissance(joueur.getFiche(listeJoueurs[j]),numJoueurInterroge,\
                                              num,cat,ficheIndices.NEPOSSEDEPAS)
    return information

def reponsePassageHumain(clu,numP):
    nomPiece=jeucarte.getNomCarteParNum(cluedo.getJeuCartes(clu),carte.SALLE,numP)
    information="Souhaitez vous prendre le passage secret vers "+nomPiece+"("+str(numP)+")? (O/N)\n"
    msgErreur=""
    rep=''
    while rep not in ['O','N']:
        cluedo.afficherCluedo(clu,information+msgErreur)
        rep=input().upper()
        msgErreur="Réponse incorrecte! Veuillez taper O ou N\n"
    return rep

def getReponsePassage(clu,numP,interactif):
    if interactif:
        return reponsePassageHumain(clu,numP)
    else:
        return cluedo.reponsePassageOrdinateur(clu,numP)

def phaseDeplacement(clu):
    joueurCourant=cluedo.getJoueurCourant(clu)
    numJoueur=joueur.getNum(joueurCourant)
    courantPrincipal=joueurCourant==cluedo.getJoueurPrincipal(clu)
    courantHumain=joueur.estHumain(joueurCourant)
    passageSecret=cluedo.passageSecretJoueurCourant(clu)
    if passageSecret!=None:
        numP,lig,col=passageSecret
        rep=getReponsePassage(clu,numP,courantHumain and courantPrincipal)
        if rep=="O":
            if courantPrincipal:
                information="Vous avez choisi de prendre le passage secret vers la salle "+str(numP)+'\n'
            else:
                information="Le joueur "+str(numJoueur)+" a choisi de prendre le passage secret vers la salle "+str(numP)+'\n'
            cluedo.deplacerJoueurCourant(clu,lig,col)
            cluedo.afficherCluedo(clu,information)
            return numP

    de,distances=cluedo.jouerDe(clu)

    information=""
    messageErreur=""
    
    if courantPrincipal:
        information+="Les dés valent "+str(de)+"\n"+infoDistance(distances)+"\nVeuillez choisir votre pièce destination\n"
    # Interaction pour choisir une destination
    fini1=False
    while not fini1:
        cluedo.afficherCluedo(clu,messageErreur+information)
        lig,col=getDestination(clu,distances,courantHumain and courantPrincipal)
        fini1=lig!=-1
        messageErreur="ATTENTION! Cette pièce n'existe pas\n"
    
    numP=cluedo.deplacerJoueurCourant(clu,lig,col)
    return numP

def phaseSolution(clu):
    joueurCourant=cluedo.getJoueurCourant(clu)
    numJoueurCourant=joueur.getNum(joueurCourant)
    jeu=cluedo.getJeuCartes(clu)
    courantPrincipal=joueurCourant==cluedo.getJoueurPrincipal(clu)
    courantHumain=joueur.estHumain(joueurCourant)
    messageErreur=""
    information=""
    if courantPrincipal:
        debutInformation="Vous êtes dans la pièce "+jeucarte.getNomCarteParNum(jeu,carte.SALLE,cluedo.getNumPieceHypothese(clu))+\
        '\nVeuillez formuler votre réponse sous la forme numProf,numMat,numSalle\n'
    else:
        debutInformation="Le joueur "+ str(numJoueurCourant)+" est dans la pièce "+\
            jeucarte.getNomCarteParNum(jeu,carte.SALLE,cluedo.getNumPieceHypothese(clu))+'\n'
    # Interaction pour faire donner une solution
    fini=False
    while not fini:
        cluedo.afficherCluedo(clu,debutInformation+messageErreur+information)
        hp=getLaSolution(clu,courantPrincipal and courantHumain)
        fini=hp!=None
        messageErreur="ATTENTION! vous n'avez pas formulé votre solution correctement\n"
    
    if courantPrincipal:
        information="Vous pensez que\n"
    else:
        information="Il pense que\n"
    information+=jeucarte.getNomCarteParNum(jeu,1,hp[0]) +" donnera un cours de "+\
        jeucarte.getNomCarteParNum(jeu,2,hp[1])+" dans la pièce "+jeucarte.getNomCarteParNum(jeu,3,hp[2])+"\n"                                                    
    fini=hp==cluedo.getSolution(clu)
    if fini:
        information+=" et c'est la bonne réponse !"
        showinfo('CLUEDO', "BRAVO C'EST GAGNE")
    else:
        information+=" et ce n'est pas la bonne réponse !!"
        cluedo.elimineJoueurCourant(clu)
        
    cluedo.afficherCluedo(clu,debutInformation+information)

    return fini 
    
    
def phaseHypothese(clu,numP):
    joueurCourant=cluedo.getJoueurCourant(clu)
    numJoueurCourant=joueur.getNum(joueurCourant)
    jeu=cluedo.getJeuCartes(clu)
    courantPrincipal=joueurCourant==cluedo.getJoueurPrincipal(clu)
    courantHumain=joueur.estHumain(joueurCourant)
    information=""
    messageErreur=""
    if courantPrincipal:
        debutInformation="Vous êtes dans la pièce "+jeucarte.getNomCarteParNum(jeu,carte.SALLE,numP)+'\n'+\
            'Entrez votre hypothèse sous la forme p,m\n'
        information=jeucarte.stringCat(jeu,carte.PROFESSEUR)+'\n'+jeucarte.stringCat(jeu,carte.MATIERE)+'\n'
    else:
        debutInformation="Le joueur "+str(numJoueurCourant)+ " est dans la pièce "+jeucarte.getNomCarteParNum(jeu,carte.SALLE,numP)+'\n'

    # Interaction pour faire une hypothèse
    fini=False
    while not fini:
        cluedo.afficherCluedo(clu,debutInformation+messageErreur+information)
        hp=getHypothese(clu,numP,courantPrincipal and courantHumain)
        fini=hp!=None
        messageErreur="ATTENTION! vous n'avez pas formulé votre hypothèse correctement\n"
    
    if courantPrincipal:
        information="Vous pensez que\n"
    else:
        information="Il pense que\n"
    information+=jeucarte.getNomCarteParNum(jeu,1,hp[1]) +" donnera un cours de "+\
        jeucarte.getNomCarteParNum(jeu,2,hp[2])+" dans la pièce "+jeucarte.getNomCarteParNum(jeu,3,hp[3])+"\n"                                                    
    cluedo.afficherCluedo(clu,debutInformation+information)
    input()
    # interrogation des joueurs sur cette hypothèse
    information+=interrogerJoueurs(clu,hp)
    cluedo.afficherCluedo(clu,debutInformation+information)
    input()

def jouer(clu):
    joueurCourant=cluedo.getJoueurCourant(clu)
    if joueur.estElimine(joueurCourant):# le joueur est éliminé donc il ne peut plus jouer
        return False
    # le joueur courant n'est pas éliminé
    numP=phaseDeplacement(clu)
    
    # suite du tour
    if numP==cluedo.getNumPieceHypothese(clu): #on est dans la pièce permettant de tenter de gagner
        res= phaseSolution(clu)
    elif numP>0 : # on est dans une autre pièce 
        phaseHypothese(clu,numP)
        res= False
    else:
        res= False
    cluedo.incNumTour(clu)
    return res

if __name__ == '__main__':
    clu=cluedo.Cluedo('Data/joueurs.csv','Data/cartes.csv','Data/plan1.csv')
    cluedo.afficherCluedo(clu,"La partie commence")
    gagne=False
    while not gagne and cluedo.getNbJoueursActifs(clu)!=0:
        gagne=jouer(clu)
    if not gagne:
        cluedo.afficherCluedo(clu, "Tous les joueurs sont éliminés!")
