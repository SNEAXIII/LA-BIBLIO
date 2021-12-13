## CLASS GRAPHE

class Graphe:
    """un graphe défini comme un disctionnaire d'adjacence"""

    def __init__(self, n):
        self.adj = {}

    def ajouterSommet(self, s):
        """ajoute au graphe un nouveau sommet s"""
        self.adj[s] = set()

    def ajouterArete(self, s1, s2):
        """crée l'arete orientée s1->s2, en créeant si besoin est le/s sommet/s manquant"""
        keys_ = set(keys_ for keys_ in self.adj)
        if not s1 in keys_: self.ajouterSommet(s1)
        if not s2 in keys_: self.ajouterSommet(s2)
        self.adj[s1].add(s2)

    def lier(self, s1, s2):
        self.ajouterArete(s1, s2)
        self.ajouterArete(s2, s1)

    def arete(self, s1, s2):
        """teste si l'arete orientée s1->s2 existe"""
        if s2 in self.adj[s1]: return True
        return False

    def sommets(self):
        """renvoie al liste des sommets qui composent le graphe"""
        return set(keys_ for keys_ in self.adj)

    def voisins(self, s):
        """renvoie la liste des sommets voisins de s"""
        return self.adj[s]

    def supprArete(self, s1, s2):
        """supprime l'arete de s1 -> s2"""
        self.adj[s1].discard(s2)

    def supprSommet(self, s):
        """supprime le sommet s du dictionnaire"""
        del (self.adj[s])

    def afficher(self):
        """affiche les sommets avec leurs voisins selon la représentation choisie"""

        for a in list(self.adj.items()):
            print(a)

## CLASS CELLULE

class Cellule:
    """ définit la classe Cellule
    valeur : attribut qui contient le premier élément
    suivante : attribut qui contient la suite de la liste"""
    def __init__(self,v,n):
        self.valeur = v
        self.suivante = n

    def __str__(self):
        return str(self.valeur)

    def print_lstc(l,rez=""):
        """fonction qui renvoie une chaine de caractères avec les éléments de la liste"""
        while not l is None: rez, l = rez + str(f"[{l.valeur}] "), l.suivante
        return rez

    def concatenerListe(self, l2):
        if self is None :
            return l2
        return Cellule(self.valeur, self.concatenerListe(self.suivante, l2))

## CLASS PILE

class Pile:
    def __init__(self):
        self.contenu = None

    def empiler(self, x):
        self.contenu = Cellule(x, self.contenu)

    def estVide(self):
        return self.contenu is None

    def depiler(self):
        if self.contenu is None:
            raise IndexError("Vous dépilez une liste vide !")

        val = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return val

