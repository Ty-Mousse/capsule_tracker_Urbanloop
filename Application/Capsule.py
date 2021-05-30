from coordonates import get_coordonates

# Définission de la classe capsule permettant de stocker les données importantes pour chaque capsules à afficher
class Capsule():
    
    # Constructeur de la classe répertoriant les données importantes
    def __init__(self, abs_initiale):
        self.abs_initiale = abs_initiale
        self.abs_curviligne = abs_initiale
        self.x, self.y = get_coordonates(abs_initiale)
        self.vitesse = 0
        self.consommation = 0
    
    # Méthode permettant la mise à jour des informations de la capsule
    def update_data(self, abs_curviligne, vitesse, consommation = 0):
        self.abs_curviligne = abs_curviligne
        self.x, self.y = get_coordonates(abs_curviligne)
        self.vitesse = vitesse
        self.consommation = consommation

    # Méthode permettant le calcul de la vitesse
    def calcul_vitesse(self):
        pass

    # Méthode permettant le calcul de la consommation
    def calcul_consommation(self):
        pass