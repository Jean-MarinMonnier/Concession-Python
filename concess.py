tabMarque = ["audi", "mercedes", "bmw", "lamborghini" ,"porsche", "ferrari", "tesla"]
tabModele = ["R8","S5", "RS4","Q8","G63", "C63","SLS", "M3", "M4", "M5", "X6", "aventador", "huracan", "urus", "macan", "911 GT3 RS", "458 italia", "F8 tributo", "model S", "model X"]
tabCouleur =  ["rouge", "bleu", "vert", "jaune", "noir", "gris", "blanc",]

class concess :
    def __init__(self, couleur, prix, marque, modele, puissance, nbPorte) :
        self.couleur = couleur
        self.prix = prix
        self.marque = marque
        self.modele = modele
        self.puissance = puissance
        self.nbPorte = nbPorte

if __name__ == "__main__":
    t = concess(input("Choisissez une couleur"), int(input("Choisissez un prix")), input("Choisissez une marque"),input("Choisissez un modèle"), int(input("Choisissez une puissance")), int(input("Choisissez le nombre de porte")))
    if t.marque != tabMarque :
        print("Nous n'avons de voiture de cette marque dans notre concession")
    elif t.couleur != tabCouleur :
        print("Nous n'avons de voiture de cette couleur dans notre concession")
    elif t.modele != tabModele :
        print("Nous n'avons ce modèle de voiture dans notre concession")
    
        