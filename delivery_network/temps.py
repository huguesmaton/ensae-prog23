from graph import *
from time import perf_counter
import numpy as np

data_path = "input/"
file_name1 = "network.1.in"
file_name2 = "routes.1.in"


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



#On utilise le module time
def calcul_temps_min_power():

    g = graph_from_file(data_path + file_name1)
    trajets = route_from_file(data_path + file_name2)
    nb_trajets = len(trajets)
    trajets = trajets[0:50] #Comme suggéré dans l'énoncé, on calcul le temps pour quelques trajets seulement puis on fait une moyenne
    t0 = perf_counter()
    for trajet in trajets:
        src, dest = trajet[0], trajet[1]
        g.min_power(src, dest)
    t1 = perf_counter()
    temps_moy = (t1 - t0)/50
    temps_tot = temps_moy * nb_trajets
    print(temps_tot)


def calcul_temps_min_power_acm_naif():

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


def calcul_temps_kruskal(): 

    g = graph_from_file(data_path + file_name1)
    t0 = perf_counter()
    kruskal(g)
    t1 = perf_counter()
    print(t1 - t0)


def calcul_temps_min_power_opti():

    num_trajets = 50
    g = graph_from_file(data_path + file_name1)
    g = kruskal(g)
    trajets = route_from_file(data_path + file_name2)
    nb_trajets = len(trajets)
    trajets = trajets[0:num_trajets]
    t0 = perf_counter()
    for trajet in trajets:
        src, dest = trajet[0], trajet[1]
        g.min_power_opti(src, dest)
    t1 = perf_counter()
    temps_moy = (t1 - t0)/num_trajets
    temps_tot = temps_moy * nb_trajets
    print(temps_tot)

def calcul_temps_min_power_LCA():

    num_trajets = 50
    g = graph_from_file(data_path + file_name1)
    g = kruskal(g)
    trajets = route_from_file(data_path + file_name2)
    nb_trajets = len(trajets)
    trajets = trajets[0:num_trajets]
    t0 = perf_counter()
    for trajet in trajets:
        src, dest = trajet[0], trajet[1]
        min_power_lca(g,src, dest)
    t1 = perf_counter()
    temps_moy = (t1 - t0)/num_trajets
    temps_tot = temps_moy * nb_trajets
    print(temps_tot)


calcul_temps_min_power_LCA()