# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module ficheIndices.py
   ~~~~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la fiche indice des joueurs. 
"""
import carte
import jeucarte
import joueur
import random
import cluedo


# constantes utilisées pour les indications dans la fiche
NESAISPAS='?'
POSSEDE='+'
NEPOSSEDEPAS='-'

#-----------------------------------------
# fonction annexe pour le constructeur
#-----------------------------------------

def creerIndications(listeNumJoueurs):
    """
    retourne un dictionnaire dont les clés sont des numéros de joueur et les valeurs NESAISPAS pour toutes les clés
    paramètre: listeJoueurs une liste d'entiers strictement positifs donnant les numéros de joueurs
               engagés dans la partie
    retourne le dictionnaire décrit ci-dessus
    """
    dico = {}
    for i in listeNumJoueurs:
        dico[i] = NESAISPAS
    return dico



#-----------------------------------------
# contructeur
#-----------------------------------------

def FicheIndices(_listeJoueurs,_jeuCartes):
    """
    retourne une fiche indices
    paramètres: _listeJoueurs: la liste des joueurs participant à la partie
                _jeuCartes: le jeu de cartes qui sera distribué aux joueurs
    exemple = {
        prof1 : {1:'?', 2:'?',3:'?',4:'?'},
        prof2 : {1:'?', 2:'?',3:'?',4:'?'},
        prof3 : {1:'?', 2:'?',3:'?',4:'?'},
        salle1 : {1:'?', 2:'?',3:'?',4:'?'},
        salle2 : {1:'?', 2:'?',3:'?',4:'?'},
        matiere1 : {1:'?', 2:'?',3:'?',4:'?'},
        matiere2 : {1:'?', 2:'?',3:'?',4:'?'},
        matiere3 : {1:'?', 2:'?',3:'?',4:'?'},
        matiere4 : {1:'?', 2:'?',3:'?',4:'?'}
    }
    """
    listeNumJoueurs = []
    for joueurs in _listeJoueurs:
        numJoueur = joueur.getNum(joueurs)
        listeNumJoueurs.append(numJoueur)
    ficheIndices = {}
    for cartes in _jeuCartes:
        if carte.getNum(cartes)!=cluedo.getNumPieceHypothese(1):
            ficheIndices[cartes] = creerIndications(listeNumJoueurs)
    return ficheIndices

def getJeuCartes(ficheIndices):
    """
    retourne le jeu de cartes associé à la fiche indice
    ficheIndices : la fiche considérée
    """
    jeuCartes = jeucarte.JeuCarte()
    for cartes in ficheIndices:
        jeucarte.addCarte(jeuCartes, cartes)
    return sorted(jeuCartes, key = carte.getNum)
    

def getListeNumJoueurs(ficheIndices):
    """
    retourne la liste des numéros des joueurs répertoriés dans la fiche
    Cette liste doit être triée dans l'ordre croissant
    ficheIndices : la fiche considérée
    """
    for listeNumJoueurs in ficheIndices.values():
        return sorted(listeNumJoueurs)

def connaissance(ficheIndices,numJoueur,numCarte,numCategorie,indication):
    """
    met à jour la fiche indice d'un joueur en fonction des informations qu'il vient de constater c-à-d
      * soit le joueur numJoueur possède la carte identifiée par numCarte numCategorie
      * soit le joueur numJoueur ne possède pas la carte identifiée par numCarte numCategorie
    paramètres: ficheIndices la fiche considérée
                numJoueur le numéro du joueur qui a montré ou qui a indiqué ne pas avoir la carte
                numCarte le numéro de la carte concernée
                numCategorie le numéro de la catégorie de la carte concernée
                indication soit POSSEDE soit NEPOSSEDEPAS
    cette fonction ne retourne rien mais elle modifie la fiche concernée en fonction des indications
    """
    carte=jeucarte.getCarteParNum(getJeuCartes(ficheIndices),numCategorie,numCarte)
    if indication=="+":
        for num_joueur in getListeNumJoueurs(ficheIndices):
            ficheIndices[carte][num_joueur]='-'
    ficheIndices[carte][numJoueur]=indication

def initFicheIndices(ficheIndices,numJoueur,jeuCartes):
    """
    initialise une fiche indice appartenant au joueur numJoueur qui possède les carte contenu dans la liste
    paramètres : ficheIndices la fiche indice du joueur
                 numJoueur un entier strictement positif indiquant le numéro de joueur à qui appartient la fiche
                 jeuCartes les cartes en possession du joueur
    cette fonction ne retourne pas de résultat mais modifie la fiche du joueur de telle sorte qu'elle indique que le joueur
    numJoueur possède chacune des cartes de la liste (et que donc les autres joueurs ne les possèdent pas)
    """
    for cartes_total in getJeuCartes(ficheIndices):
        connaissance(ficheIndices, numJoueur, carte.getNum(cartes_total), carte.getCategorie(cartes_total), '-')
    for cartes in jeuCartes:
        for numjoueur in ficheIndices[cartes].keys():
            connaissance(ficheIndices, numjoueur, carte.getNum(cartes), carte.getCategorie(cartes), '-')
            if numjoueur==numJoueur:
                connaissance(ficheIndices, numjoueur, carte.getNum(cartes), carte.getCategorie(cartes), '+')

# --------------------------------------------------------------#
# La partie ci-dessus doit être implémentée pour le 21 décembre #
# --------------------------------------------------------------#

def getIndication(ficheIndices,numJoueur,numCategorie,numCarte):
    """
    retourne l'indication que l'on possède concernant le joueur numJoueur et la carte numCarte,numCategorie
    paramètres: ficheIndices la fiche considérée
                numJoueur le numéro du joueur qui a montré ou qui a indiqué ne pas avoir la carte
                numCarte le numéro de la carte concernée
                numCategorie le numéro de la catégorie de la carte concernée
    resultat une des trois indications POSSEDE, NEPOSSEDEPAS ou NESAISPAS
    """
    return ficheIndices[jeucarte.getCarteParNum(getJeuCartes(ficheIndices),numCategorie,numCarte)][numJoueur]


def estConnue(ficheIndices,numCarte,numCategorie):
    """
    indique si pour une carte donnée soit on sait qu'elle appartient à l'un des joueurs
                                     soit on sait qu'elle n'appartient à personne
    paramètres: ficheIndices la fiche considérée
                numCarte le numéro de la carte concernée
                numCategorie le numéro de la catégorie de la carte concernée
    résultat un booléen indiquant si on sait définitivement si la carte appartient à un joueur ou à personne
    """
    nombre_possede_pas=0
    for indic in ficheIndices[jeucarte.getCarteParNum(getJeuCartes(ficheIndices),numCategorie,numCarte)].values():
        if indic=='+':
            return True
        if indic=='?':
            return False
    return True

def estDansLeMystere(ficheIndices,numCarte,numCategorie):
    """
    indique si on est sûr que la carte est dans le mystère
    paramètres: ficheIndices la fiche considérée
                numCarte le numéro de la carte concernée
                numCategorie le numéro de la catégorie de la carte concernée
    résultat un booléen indiquant si on sait définitivement que la carte n'appartient à personne
    """
    est_sur=estConnue(ficheIndices,numCarte,numCategorie)
    if est_sur:
        if ficheIndices[jeucarte.getCarteParNum(getJeuCartes(ficheIndices),numCategorie,numCarte)][0]=='-':
            return True
    return False
   
def listeCartesInconnues(ficheIndices,categorie):
    """
    retourne la liste des numéros de cartes d'une certaine catégorie pour lesquelles on n'a pas de certitude
    paramètres: ficheIndices la fiche considérée
                categorie le numéro de la catégorie recherchée
    résultat la liste des numéros de carte de la catégorie pour lesquelles on n'a pas de certitude
    """
    liste_num_cat=jeucarte.getListeNumCarteCategorie(getJeuCartes(ficheIndices),categorie)
    pas_de_certitude=[]
    for numCarte in liste_num_cat:
        if not estConnue(ficheIndices,numCarte,categorie):
            pas_de_certitude.append(numCarte)
    return pas_de_certitude


def listeCartesJoueur(ficheIndices,categorie,numJoueur):
    """
    retourne la liste des numéros de cartes d'une catégorie que l'on sait possédées par le joueur numJoueur
    paramètres: ficheIndices la fiche considérée
                numCategorie le numéro de la catégorie cherchée
                numJoueur le joueur dont on recherche les cartes
    résultat la liste des numéros cartes de la catégorie pour lesquelles on a la certitude que le joueur numJoueur la possède
    """
    jeuCarte=getJeuCartes(ficheIndices)
    liste_num_cat=jeucarte.getListeNumCarteCategorie(jeuCarte,categorie)
    certitude=[]
    for numCarte in liste_num_cat:
        if ficheIndices[jeucarte.getCarteParNum(jeuCarte,categorie,numCarte)][numJoueur]=='+':
            certitude.append(numCarte)
    return certitude


def hypothesesSures(ficheIndices):
    """
    retourne un dictionnaire dont les clés sont les catégories de carte et les valeurs la carte de la
    catégorie correspondante que l'on sait être dans la solution. Si on n'a aucune certitude pour une 
    catégorie, la clé ne sera pas présente dans le dictionnaire.
    paramètres: ficheIndices la fiche considérée
    résultat le dictionnaire décrit ci dessus
    """
    dico_hypothese={}
    jeuCarte=getJeuCartes(ficheIndices)
    for categorie in range(1,4):
        liste_num_carte=jeucarte.getListeNumCarteCategorie(jeuCarte,categorie)
        for num_carte in liste_num_carte:
            if estDansLeMystere:
                dico_hypothese[categorie]=jeucarte.getCarteParNum(jeuCarte,categorie,num_carte)
    return dico_hypothese


def choixCartes(ficheIndices, numJoueur, numCategorie):
    """
    retourne une liste de numéros de carte d'une certaine catégorie pouvant être
    utilisée pour émettre une hypothèse intéressante pour le joueur numJoueur
    paramètres: ficheIndices la fiche considérée
                numJoueur le joueur dont on recherche les cartes
                numCategorie le numéro de la carte cherchée
    résultat la liste des numéros de cartes de la catégorie intéressant pour le joueur numJoueur
    """
    nombre = random.randint(1, 5)
    if nombre == 1:
        return listeCartesInconnues(ficheIndices, numCategorie) + listeCartesJoueur(ficheIndices, numCategorie, numJoueur)
    return listeCartesInconnues(ficheIndices, numCategorie)



def creerUneHypothese(ficheIndices,numJoueur,numSalle):
    """
    retourne un couple numProf, numMat indiquant les cartes choisies comme hypothèse. 
    La salle est fixée par numSalle 
    paramètres: ficheIndices la fiche considérée
                numJoueur le joueur qui formule l'hypothèse
                numSalle le numéro de la salle dans laquelle se trouve le joueur
    """
    interessantProf=choixCartes(ficheIndices,numJoueur,1)
    interessantMatiere=choixCartes(ficheIndices,numJoueur,2)
    random.shuffle(interessantProf)
    random.shuffle(interessantMatiere)
    return (interessantProf[0],interessantMatiere[0],numSalle)


#-----------------------------------------
# entrees-sorties
#-----------------------------------------

def string(ficheIndices):
    """
    Transforme une fiche indice en une chaine de caractères
    paramètre:  ficheIndices la fiche considérée 
    """
    jeu=getJeuCartes(ficheIndices)
    listeNumJoueur=getListeNumJoueurs(ficheIndices)
    
    res=" "*34+"Fiche Indices\n"
    res+=carte.categorieFromNum(carte.PROFESSEUR).ljust(38+len(listeNumJoueur)*2)+carte.categorieFromNum(carte.MATIERE).ljust(38)+"\n"
    for x in range(2):
        res+=' '*36
        for n in listeNumJoueur:
            res+=str(n)+' '        
    res+='\n'
    lesNum=jeucarte.getListeNumCarteCategorie(jeu,carte.PROFESSEUR)
    lesNum.sort()
    lesNum2=jeucarte.getListeNumCarteCategorie(jeu,carte.MATIERE)
    lesNum2.sort()
    for x in range(max(len(lesNum),len(lesNum2))):
        if x<len(lesNum):
            res+=(str(lesNum[x]).rjust(2)+'. '+jeucarte.getNomCarteParNum(jeu,carte.PROFESSEUR,lesNum[x])).rjust(34)+': '
            for j in listeNumJoueur:
                res+=getIndication(ficheIndices,j,carte.PROFESSEUR,lesNum[x])+' '
        else:
            res+=' '*(34+len(listeNumJoueur)*2)
        if x<len(lesNum2):
            res+=(str(lesNum2[x]).rjust(2)+'. '+jeucarte.getNomCarteParNum(jeu,carte.MATIERE,lesNum2[x])).rjust(34)+': '
            for j in listeNumJoueur:
                res+=getIndication(ficheIndices,j,carte.MATIERE,lesNum2[x])+' '
        res+='\n'
    
    res+=carte.categorieFromNum(carte.SALLE).ljust(34)+"\n"
    res+=' '*36
    for j in listeNumJoueur:
        res+=str(j)+' '
    res+='\n'
    lesNum=jeucarte.getListeNumCarteCategorie(jeu,carte.SALLE)
    lesNum.sort()
    for i in lesNum:
        res+=(str(i).rjust(2)+'. '+jeucarte.getNomCarteParNum(jeu,carte.SALLE,i)).rjust(34)+': '
        for j in listeNumJoueur:
            res+=getIndication(ficheIndices,j,carte.SALLE,i)+' '
        res+='\n'
    return res
