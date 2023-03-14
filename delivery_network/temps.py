from graph import Graph, graph_from_file, UnionFind, kruskal
from time import perf_counter

data_path = "input/"
file_name1 = "network.1.in"
file_name2 = "routes.1.in"

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




def calcul_temps_min_power(): #Pour le network.1

    g = graph_from_file(data_path + file_name1)
    trajets = route_from_file(data_path + file_name2)
    nb_trajets = len(trajets)
    trajets = trajets[0:10]
    t0 = perf_counter()
    for trajet in trajets:
        src, dest = trajet[0], trajet[1]
        g.min_power(src, dest)
    t1 = perf_counter()
    temps_moy = (t1 - t0)/10
    temps_tot = temps_moy * nb_trajets
    print(temps_tot)


def calcul_temps_min_power_acm_naif(): #Pour le network.1

    g = graph_from_file(data_path + file_name1)
    trajets = route_from_file(data_path + file_name2)
    nb_trajets = len(trajets)
    trajets = trajets[0:10]
    t0 = perf_counter()
    for trajet in trajets:
        src, dest = trajet[0], trajet[1]
        g.min_power_acm_naif(src, dest)
    t1 = perf_counter()
    temps_moy = (t1 - t0)/10
    temps_tot = temps_moy * nb_trajets
    print(temps_tot)


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


calcul_temps_min_power_acm()
