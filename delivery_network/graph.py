import numpy as np

class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output


    #QUESTION 1 partie 1 : Solution du professeur
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1
    

    #QUESTION 3 : 
    def get_path_with_power(self, src, dest, power):
        deja_visites = []

        return chemins(self, src, [src], dest, deja_visites, power) #On appelle chemins sur le noeud source (voir en bas les fonctions auxiliaires)
    #Le graphe est parcouru une seule fois donc la compléxité est en O(V*E) dans le pire des cas


    #QUESTION 2 : On commence par écrire une fonction connected_componenents qui renvoie la liste des composantes connexes d'un graphe
    def connected_components(self):
        composantes_connexes = []
        deja_visites = []

        for node1 in self.nodes: #On parcours le graphe : on effectue un parcours en profondeur a partir d'un noeud ssi le noeud n'a pas encore été visité
            if node1 not in deja_visites:
                composantes_connexes.append(parcours_profondeur(self, node1, deja_visites)) #On appelle une fonction auxiliare (voir en bas)
        return composantes_connexes
        #Ainsi chaque noeud est parcouru une unique fois, la complexité est donc en O(V + E))

    #Cette fonction transforme la liste des composantes connéctées en frozenset
    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    

    #QUESTION 6 : 
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        n = 1
        gauche = 0
        droite = 2
        #On initialise des valeurs que l'on va utiliser pour la dichotomie

        while self.get_path_with_power(src, dest, droite) == None: #Tant que la puissance minimale n'est pas d'ans l'intervalle [gauche, droite], on augmente n
            n += 1
            gauche = 2**(n-1)
            droite = 2**n
            
        return dichotomie(self, gauche, droite, src, dest) #On appelle la dichotomie sur les valeurs initialisés (voir fonctions auxiliaires en bas)

    #La dichotomie est en O(log(droite - gauche)). On commence par chercher le bon intervalle de la forme [2**(n-1), 2**n] en appelant la fonction get_path_with_power. 
    #Donc c'est un O(n), ou n est tq 2**n > puissance max dans le graphe > 2**(n-1).
    #Mais ici on appelle get_path_with_power dans la dichotomie donc la compléxité est O(n*nb_nodes).
    #Pour nb_nodes grand, la compléxité de ce while est un O(nb_nodes) car on va l'appeller k fois et si nb_nodes est grand O(k*nb_nodes) = O(nb_nodes).
    #La compléxité est donc un O(n*nb_nodes + nb_nodes) = O(nb_nodes) pour nb_nodes grand. 
    #REMARQUE : on aurait pu faire la dichotomie sur la liste triée des puissances. Dans le MEILLEUR des cas si le graphe est connexe, le nombre d'aretes est de l'ordre du nombre
    #de noeud et donc trier cette liste est de compléxité O(nb_nodes*log(nb_nodes)). Ceci étant pour le meilleur des cas, on voit bien que cette méthode n'est pas optimale
    

    #QUESTION 14 : Première version naive ou on utilise les fonctions precedentes (non optimisées pour des MST) sur le MST donné par kruskal
    #Ce n'est toujours pas satisfaisant cf fichier temps.py fonction calcul_temps_min_power_acm_naif
    def min_power_acm_naif(self, src, dest):
        self = kruskal(self)
        return self.min_power(src, dest)

    #QUESTION 14 optimisation :
    def get_path_with_power_largeur(self, src, dest, power): #Ici on effectue un parcours en largeur plutot que un parcours en profondeur
        return parcours_largeur(self, src, dest, power)


    def min_power_largeur(self, src, dest): #On réutilise la min_power de la question 6 en utilisant get_path_with_power_acm
        n = 1
        gauche = 0
        droite = 2

        while self.get_path_with_power_largeur(src, dest, droite) == None: 
            n += 1
            gauche = 2**(n-1)
            droite = 2**n
            
        return dichotomie_largeur(self, gauche, droite, src, dest)


    def min_power_acm(self, src, dest): #Finalement, on definit cette fonction qui est optimisé pour les arbres
        self = kruskal(self)
        return self.min_power_largeur(src, dest)
    
    
    '''
    def get_path_with_power_largeur_rec(self, src, dest, power):
        chemin = []
        deja_visites = set()
        booleen, power = parcours_largeur_rec(self, src, dest, chemin, deja_visites, power)
        
        return chemin, power
    '''

    def min_power_opti(self, src, dest):
        self = kruskal(self)
        power = np.inf
        chemin = []
        deja_visites = set()
        booleen, power = parcours_largeur_rec(self, src, dest, chemin, deja_visites, power)
        
        return chemin, power




#QUESTION 1 partie 2 et QUESTION 4: Solution du professeur
def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    g: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min, 1) 
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g


#QUESTION 12 : Comme suggéré dans l'énoncé, on commence par implémenter la classe UnionFind
class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rang = [0] * n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        racinei, racinej = self.find(i), self.find(j)
        if racinei == racinej:
            return False
        if self.rang[racinei] < self.rang[racinej]:
            self.parent[racinei] = racinej
        elif self.rang[racinei] > self.rang[racinej]:
            self.parent[racinej] = racinei
        else:
            self.parent[racinei] = racinej
            self.rang[racinej] += 1
        return True


#Kruskal crée l'arbre minimum couvrant, on suppose donc que le graphe est connexe
def kruskal(graph):

    aretes = []
    for node1 in graph.graph:
        for node2, power_min, dist in graph.graph[node1]:
            if node1 < node2:
                aretes.append((power_min, node1, node2))
    aretes.sort() #On trie les aretes par poids croissant
    
    n = graph.nb_nodes
    uf = UnionFind(n + 1) #Sans la +1, on obtient une erreur Index out of range
    
    graph_acm = Graph(range(1,n+1)) #acm = arbre couvrant minimum
    for power_min, node1, node2 in aretes:
        if uf.union(node1, node2):
            graph_acm.add_edge(node1, node2, power_min) #On ajoute les aretes ssi cela ne crée pas de cycle dans le graphe
    
    return graph_acm




#FONCTIONS AUXILIAIRES

#Pour la question3 :
def chemins(g, node1, chemin, dest, deja_visites, power): #Fonction récursive qui prend en argument un noeud et le chemin suivi pour arriver jusqu'à ce noeud ainsi que le noeud destination et la liste des noeuds visites et la power
    if node1 == dest: #Si le node1 est la destination alors c'est fini
        return chemin
    for triple in g.graph[node1]: #On parcours les voisins de node1
        node2, power_min, dist = triple
        if node2 not in deja_visites and power_min <= power: #On vérifie les conditions, notamment sur la puissance minimale
            deja_visites.append(node2)
            cheminrec = chemins(g, node2, chemin+[node2], dest, deja_visites, power) #On appelle récursivement la fonction sur chaque voisin
            if cheminrec is not None:
                return cheminrec
    return None #Si tout les voisisns ont été visité, et donc recursivement tous les noeuds de la composante connexe du noeud node1, alors il n'y a pas de chemin possible, on renvoie None


#Pour la question2 :
def parcours_profondeur(g, node1, deja_visites): #On écrit une fonction parcours en profondeur
    composante_node1 = [node1]
    for triple in g.graph[node1]:
        node2 = triple[0]
        if node2 not in deja_visites:
            deja_visites.append(node2)
            composante_node1 += parcours_profondeur(g, node2, deja_visites)
    return composante_node1


#Pour la question6 :
def dichotomie(g, gauche, droite, src, dest): #Fonction dichotomie qui prend en argument la borne inf et sup d'un intervalle
    while abs(droite - gauche) > 1: #On souhaite droite = gauche
        milieu = (droite + gauche)/2 #On travaille avec gauche et droite puissances de 2 donc milieu est toujours un entier
        if g.get_path_with_power(src, dest, milieu) != None:
            droite = milieu
        else:
            gauche = milieu
        dichotomie(g, gauche, droite, src, dest)
    return g.get_path_with_power(src, dest, droite), droite

def dichotomie_largeur(g, gauche, droite, src, dest): #Fonction dichotomie qui prend en argument la borne inf et sup d'un intervalle
    while abs(droite - gauche) > 1: #On souhaite droite = gauche
        milieu = (droite + gauche)/2 #On travaille avec gauche et droite puissances de 2 donc milieu est toujours un entier
        if g.get_path_with_power_largeur(src, dest, milieu) != None:
            droite = milieu
        else:
            gauche = milieu
        dichotomie_largeur(g, gauche, droite, src, dest)
    return g.get_path_with_power_largeur(src, dest, droite), droite


#Pour la question14 qui optimise la question3 :
def parcours_largeur(g, src, dest, power):
    deja_visites = set()
    queue = [[src]]
    
    if src == dest:
        return [src]

    while queue:
        chemin = queue.pop(0)
        node1 = chemin[-1]

        if node1 not in deja_visites:
            triple = g.graph[node1]
            for node2, power_min, dist in triple:
                if power_min <= power:
                    cheminbis = list(chemin)
                    cheminbis.append(node2)
                    queue.append(cheminbis)
                
                    if node2 == dest:
                        return cheminbis
            
            deja_visites.add(node1)
    
    return None

def parcours_largeur_rec(g, node1, dest, chemin, deja_visites, power):
    deja_visites.add(node1)
    chemin.append(node1)
    if node1 == dest:
        return True, 0
    for triple in g.graph[node1]:
        node2, power_min, dist = triple
        if node2 not in deja_visites and power_min <= power:
            dest_trouvee, maxpower = parcours_largeur_rec(g, node2, dest, chemin, deja_visites, power)
            if dest_trouvee:
                return True, max(maxpower, power_min)
    chemin.pop()
    return False, 0