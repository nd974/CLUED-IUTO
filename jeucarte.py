# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module 
   ~~~~~~~~~~~~~~~
   
   Ce module gère un jeu de cartes de cluedo.
   ATTENTION !!!
        il y a une carte particulière: il s'agit de la carte de
        la salle où l'on peut tenter de gagner (la salle des archives)
        En effet cette carte est là pour permettre d'avoir les informations
        sur cette pièce mais elle ne doit pas être distribuée
              
"""
import carte
import mystere
import random


test_carte3=(4,"Jrad",carte.PROFESSEUR,"Prof de AP",True)
#-----------------------------------------
# contructeur
#-----------------------------------------
def JeuCarte():
    """
    retourne un jeu de cartes vide
    """
    return []


def addCarte(jeucarte,carte):
    """
    ajoute une carte au jeu de carte
    jeuCarte : un jeu de carte 
    carte : une carte telle que définie dans carte.py
    """
    jeucarte.append(carte)

def enleverCarte(jeucarte,carte):
    """
    enlève une carte au jeu de carte
    jeuCarte : un jeu de carte 
    carte : une carte telle que définie dans carte.py
    """
    jeucarte.remove(carte)


def melangerJeu(jeucarte):
    """
    mélange de manière aléatoire un jeu de carte
    jeuCarte : un jeu de carte
    """
    random.shuffle(jeucarte)

    
def listeCartes(jeuCarte):
    """
    retourne le jeu de cartes sous la forme d'une liste de cartes
    jeuCarte : un jeu de carte
    résultat: la liste des cartes du jeu
    """
    return jeuCarte

def definirMystere(jeucarte):
    """
    retourne un mystère constitué de cartes du jeu
    ces cartes sont enlevées du jeu
    jeuCarte : un jeu de carte considéré comme mélangé
    """
    reste_mystere=[carte.PROFESSEUR,carte.MATIERE,carte.SALLE]
    i=0
    ok_matiere=False
    ok_professeur=False
    ok_salle=False
    while (not ok_matiere or not ok_professeur or not ok_salle) and i<len(jeucarte):
        if not ok_professeur and carte.getCategorie(jeucarte[i])==reste_mystere[0]:
            mystere_professeur=carte.getNum(jeucarte[i])
            ok_professeur=True
            cartes=list(jeucarte[i])
            cartes[4]=False
            jeucarte[i]=tuple(cartes)

            i-=1
        elif not ok_matiere and carte.getCategorie(jeucarte[i])==reste_mystere[1]:
            mystere_matiere=carte.getNum(jeucarte[i])
            ok_matiere=True
            cartes=list(jeucarte[i])
            cartes[4]=False
            jeucarte[i]=tuple(cartes)
            i-=1
        elif not ok_salle and carte.getCategorie(jeucarte[i])==reste_mystere[2]:
            mystere_salle=carte.getNum(jeucarte[i])
            if mystere_salle!=10:
                ok_salle=True
                cartes=list(jeucarte[i])
                cartes[4]=False
                jeucarte[i]=tuple(cartes)
                i-=1
        i+=1
    try:
        return mystere.Mystere(mystere_professeur,mystere_matiere,mystere_salle)
    except:
        print("Jeu de carte non complet")

    
def estDans(jeucarte,carte):
    """
    indique si une carte fait partie d'un jeu de carte
    jeuCarte : un jeu de carte
    carte : une carte telle que définie dans carte.py
    """
    return carte in jeucarte

def cartesDistribuables(jeucarte):
    """
    retourne un jeu carte copie de celui passé en paramètre 
    mais ne contenant pas la carte de la pièce qui permet au
    joueur de donner leur réponse à l'énigme
    jeuCarte : un jeu de carte
    """
    carte_distribuables=[]
    for cartes in jeucarte:
        if carte.estDistribuable(cartes):
            carte_distribuables.append(cartes)
    return carte_distribuables


def getCartePieceHypothese(jeucarte):
    """
    retourne la carte salle qui sert au joueur à faire leur hypothèse (c'est la seule carte non distribuable du jeu)
    jeuCarte : un jeu de carte
    """
    for cartes in jeucarte:
        if not carte.estDistribuable(cartes):
            return cartes   

def getCarteParNum(jeucarte,cat,numCarte):
    """
    recherche une carte dans le jeu à partir des numéros de
    catégorie et de carte
    jeuCarte : un jeu de carte
    cat      : le numéro de la catégorie (PROFESSEUR, MATIERE, SALLE)
    numCarte : le numéro de la carte 
    """
    for cartes in jeucarte:
        if carte.getNum(cartes)==numCarte and carte.getCategorie(cartes)==cat:
            return cartes

def getNomCarteParNum(jeucarte,cat,numCarte):
    """
    recherche le nom d'une carte dans le jeu à partir des numéros de
    catégorie et de carte
    jeuCarte : un jeu de carte
    cat      : le numéro de la catégorie (PROFESSEUR, MATIERE, SALLE)
    numCarte : le numéro de la carte 
    """
    for cartes in jeucarte:
        if carte.getNum(cartes)==numCarte and carte.getCategorie(cartes)==cat:
            return carte.getNom(cartes)

def getListeNumCarteCategorie(jeucarte,cat):
    """
    retourne la liste des numéros de carte du jeu qui sont dans
    catégorie passée en paramètre
    jeuCarte : un jeu de carte
    cat      : le numéro de la catégorie (PROFESSEUR, MATIERE, SALLE)
    """    
    liste_num_carte_cat=[]
    for cartes in jeucarte:
        if carte.getCategorie(cartes)==cat:
            liste_num_carte_cat.append(carte.getNum(cartes))
    return liste_num_carte_cat


# -----------------------------------------
#  Fonctions servant à l'affichage
# -----------------------------------------

def string(jeucarte):
    """
    retourne une chaine de caractères représentant un jeu de cartes
    jeuCarte : un jeu de carte
    """
    chaine_jeucarte=""
    for carte in jeucarte:
        chaine_jeucarte+=str(carte)+"\n"
    return chaine_jeucarte

def stringCat(jeucarte,categorie):
    """
    retourne une chaine de caractères donnant les numéros et noms des cartes
    d'une catégorie par exemple pour les professeurs on souhaite obtenir une chaine
    qui s'affiche comme ci-dessous:
    1. Edgar Codd
    2. John von Neuman
    3. Allan Turing
    4. JCR Licklider
    5. Ada Lovelace
    6. Grace Hopper
    paramètres:
    jeuCarte : un jeu de carte
    categorie : le numéro de la catégorie
    """   
    chaine_cat=''
    for cartes in jeucarte:
        if carte.getCategorie(cartes)==categorie:
            chaine_cat+=" "+str(carte.getNum(cartes))+". "+carte.getNom(cartes)+"\n"
    return chaine_cat


# -----------------------------------------
#  Fonction permettant de lire un jeu de cartes dans un fichier
# -----------------------------------------


def lireJeuCarte(nomFic):
    """
    retourne une liste de cartes en lisant un fichier texte
    chaque ligne du fichier contient les informations suivantes:
            num carte;nom carte;description carte;nom fic image
            Les catégories de cartes sont séparée par une ligne vide
    nomFic le nom du fichier où se trouve la description des cartes
    """
    texte=""
    try:
        fic=open(nomFic)
        texte=fic.read()
        fic.close()
    except:
        print("probleme de lecture du fichier")
        return []
    lignes=texte.split("\n")
    i=1
    res=JeuCarte()
    for ligne in lignes:
        erreur=False
        elements=ligne.split(";")
        if len(elements)!=5:
            print("ligne",i,"ignorée car nombre d'éléments incorrects")
        else:
            try:
                num=int(elements[0])
                nom=elements[1]
                nomcat=elements[2]
                info=elements[3]
                if carte.estNomCategorie(nomcat):
                    cat=carte.categorieFromNom(nomcat)
                else:
                    print("ligne",i,"ignorée car le nom du type de la carte n'est pas correcte")
                    erreur=True
                if not erreur:
                    if nom.endswith('!'):
                        addCarte(res,carte.Carte(num,nom,cat,info,False))
                    else:
                        addCarte(res,carte.Carte(num,nom,cat,info,True))
            except:
                print("ligne",i,"ignorée car le numéro n'a pas le bon format")
                
        i=i+1
    return res