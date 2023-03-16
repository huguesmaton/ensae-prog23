from graph import Graph, graph_from_file, UnionFind, kruskal
from time import perf_counter

data_path = "input/"
file_name1 = "network.2.in"
file_name2 = "routes.2.in"


#QUESTION 10 : On commence par transformer les fichiers routes.x.in en liste
def route_from_file(filename):

    trajets = []
    with open(filename, "r") as file:
        m = int(file.readline())
        for _ in range(m):
            trajet = list(map(int, file.readline().split()))
            if len(trajet) == 3:
                ville1, ville2, utilite = trajet
                trajets.append([ville1, ville2, utilite])
            else:
                raise Exception("Format incorrect")
    return trajets



#On utilise le module time et on appelle la fonction min_power
def calcul_temps_min_power(): #Pour le network.1

    g = graph_from_file(data_path + file_name1)
    trajets = route_from_file(data_path + file_name2)
    nb_trajets = len(trajets)
    trajets = trajets[0:10] #Comme suggéré dans l'énoncé, on calcul le temps pour quelques trajets seulement puis on fait une moyenne
    t0 = perf_counter()
    for trajet in trajets:
        src, dest = trajet[0], trajet[1]
        g.min_power(src, dest)
    t1 = perf_counter()
    temps_moy = (t1 - t0)/10
    temps_tot = temps_moy * nb_trajets
    print(temps_tot)
#Pour le network1, on obtient un temps moyen de 40 secondes. En revanche pour les autres network on n'obtient pas de résultat car les fonctions ne sont pas optimisées, d'où les questions suivantes


def calcul_temps_min_power_acm_naif(): #Pour le network.1

    g = graph_from_file(data_path + file_name1)
    trajets = route_from_file(data_path + file_name2)
    nb_trajets = len(trajets)
    trajets = trajets[0:1]
    t0 = perf_counter()
    for trajet in trajets:
        src, dest = trajet[0], trajet[1]
        g.min_power_acm_naif(src, dest)
    t1 = perf_counter()
    temps_moy = (t1 - t0)/1
    temps_tot = temps_moy * nb_trajets
    print(temps_tot)
#Pour le network1, on a divisé le temps par 2, mais on n'a toujours pas de résulat pour les autres network



def calcul_temps_min_power_acm(): #Pour le network.1

    g = graph_from_file(data_path + file_name1)
    trajets = route_from_file(data_path + file_name2)
    nb_trajets = len(trajets)
    trajets = trajets[0:10]
    t0 = perf_counter()
    for trajet in trajets:
        src, dest = trajet[0], trajet[1]
        g.min_power_acm(src, dest)
    t1 = perf_counter()
    temps_moy = (t1 - t0)/10
    temps_tot = temps_moy * nb_trajets
    print(temps_tot)


calcul_temps_min_power_acm_naif()
