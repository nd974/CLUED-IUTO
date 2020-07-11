import carteOO

class Mystere(object):
    def __init__(self,_numProf,_numMat,_numSalle):
        """
        constructeur
        """
        self._numProf=_numProf
        self._numMat=_numMat
        self._numSalle=_numSalle


    def getProfesseur(self):
        return self._numProf

    def getMatiere(self):
        return self._numMat

    def getSalle(self):
        return self._numSalle


