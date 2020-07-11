import carteOO
import mystere00
import random

class jeuCarte(object):
    def __init__(self):
        """
        constructeur
        """
        self.jeuDeCarte=[]

    def addCarte (self,carte):
        self.jeuDeCarte.append(carte)

    def enleverCarte (self,carte):
        self.jeuDeCarte.remove(carte)

    def melangerJeu (self):
        random.shuffle(self.jeuDeCarte)

    def listeCartes (self):
        return self.jeuDeCarte
    
    def definirMystere(self):
        reste_mystere=[carteOO.PROFESSEUR,carteOO.MATIERE,carteOO.SALLE]
        i=0
        ok_matiere=False
        ok_professeur=False
        ok_salle=False
        while (not ok_matiere or not ok_professeur or not ok_salle) and i<len(self.jeuDeCarte):
            if not ok_professeur and carteOO.getCategorie(self.jeuDeCarte[i])==reste_mystere[0]:
                mystere_professeur=carteOO.getNum(self.jeuDeCarte[i])
                ok_professeur=True
                self.jeuDeCarte.pop(i)
                i-=1
            elif not ok_matiere and carteOO.getCategorie(self.jeuDeCarte[i])==reste_mystere[1]:
                mystere_matiere=carteOO.getNum(self.jeuDeCarte[i])
                ok_matiere=True
                self.jeuDeCarte.pop(i)
                i-=1
            elif not ok_salle and carteOO.getCategorie(self.jeuDeCarte[i])==reste_mystere[2]:
                mystere_salle=carteOO.getNum(self.jeuDeCarte[i])
                ok_salle=True
                self.jeuDeCarte.pop(i)
                i-=1
            i+=1
        try:
            return mystere00.Mystere(mystere_professeur,mystere_matiere,mystere_salle)
        except:
            print("Jeu de carte non complet")

    def estDans (self,carte):
        return carte in self.jeuDeCarte
    
    def cartesDistribuables(self):
        carte_distribuables=[]
        for cartes in self.jeuDeCarte:
            if carteOO.estDistribuable(cartes):
                carte_distribuables.append(cartes)
        return carte_distribuables
    
    def getCartePieceHypothese(self):
        for cartes in self.jeuDeCarte:
            if not carteOO.estDistribuable(cartes):
                return cartes

    def getCarteParNum(self,cat,numCarte):
        for cartes in self.jeuDeCarte:
            if carteOO.getNum(cartes)==numCarte and carteOO.getCategorie(cartes)==cat:
                return cartes

    def getNomCarteParNum(self,cat,numCarte):
        for cartes in self.jeuDeCarte:
            if carteOO.getNum(cartes)==numCarte and carteOO.getCategorie(cartes)==cat:
                return carteOO.getNom(cartes)

    def getListeNumCarteCategorie(self,cat):  
        liste_num_carte_cat=[]
        for cartes in self.jeuDeCarte:
            if carteOO.getCategorie(cartes)==cat:
                liste_num_carte_cat.append(carteOO.getNum(cartes))
        return liste_num_carte_cat

    def string(self):
        chaine_self.jeuDeCarte=""
        for cartes in self.jeuDeCarte:
            chaine_self.jeuDeCarte+=str(cartes)+"\n"
        return chaine_self.jeuDeCarte

    def stringCat(self,categorie):
        chaine_cat=''
        for cartes in self.jeuDeCarte:
            if carteOO.getCategorie(cartes)==categorie:
                chaine_cat+=" "+str(carteOO.getNum(cartes))+". "+carteOO.getNom(cartes)+"\n"
        return chaine_cat


def lirejeuDeCarte(nomFic):
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
    res=jeuCarte()
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
                if carteOO.estNomCategorie(nomcat):
                    cat=carteOO.categorieFromNom(nomcat)
                else:
                    print("ligne",i,"ignorée car le nom du type de la carte n'est pas correcte")
                    erreur=True
                if not erreur:
                    if nom.endswith('!'):
                        jeuCarte.addCarte(res,carteOO.Carte(num,nom,cat,info,False))
                    else:
                        jeuCarte.addCarte(res,carteOO.Carte(num,nom,cat,info,True))
            except:
                print("ligne",i,"ignorée car le numéro n'a pas le bon format")
                    
        i=i+1
    return res

if __name__=='__main__':
    lirejeuDeCarte("../Data/cartes.csv")
