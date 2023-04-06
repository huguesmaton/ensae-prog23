from graph import *


numero = 1
budget = 25*(10**9)
filename = "input/trucks." + str(numero) + ".in"
g = graph_from_file("input/network." + str(numero) + ".in")
g = kruskal(g)
trucks = trucks_from_file(filename)
trips = routes_out(numero)

#Fonction qui sélectionne seulement les camions utiles :
#On retire les camions avec une puissance plus faible mais un cout plus grand par comparaison à un autre camion
def camions_utiles(trucks): 
    trucks.sort(key=lambda camions_utiles : camions_utiles[1]) #Tri par cout croissant
    utiles = []
    power = 0 
    for truck in trucks:
        if power < truck[0]: #Les camions étant triés par cout croissant, on ne prend pas les camions avec une puissance plus faible
            utiles.append(truck)
            power = truck[0]
    return utiles
    #print(len(trucks), len(camions_utiles(trucks))) renvoie (10000,185) donc cette fonction est très importante

#Approche "glouton" de la recherche du meilleur profit
def algo_glouton(trucks, trips, budget):

    trucks = camions_utiles(trucks) #Les camions sont rangés par couts croissants
    
    trips = sorted(trips, key=lambda r: r[2], reverse=True) #On trie les routes par profit décroissant
    
    assignations = {} #On renvoie un dictionnaire qui a un trajet (src, dest) assigne un camion (puissance, cout) 
    budget_tot = 0
    
    for route in trips: #On parcourt les trajet et pour chaque trajet, on choisit le meilleur camion
        start, end, profit, power_min = route
        
        for truck in trucks:
            power, cout = truck
            
            if power >= power_min and budget_tot + cout <= budget:
                assignations[(start, end)] = truck
                budget_tot += cout
                break
        
    return assignations

print(algo_glouton(trucks, trips, budget))