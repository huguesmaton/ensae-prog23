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

    trucks = camions_utiles(trucks)
    trucks = sorted(trucks, key=lambda t: t[0], reverse=True) #On trie les camions par puissance décroissante
    
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



def algo_knapsack(routes, trucks, budget):
    # Tri des camions par coût croissant
    trucks = sorted(trucks, key=lambda x: x[1])
    # Initialisation du tableau de résultat
    result = [0] * (budget + 1)
    # Boucle sur les routes
    for route in routes:
        # Boucle sur les camions
        for truck in trucks:
            # Vérification que le camion peut être utilisé pour cette route
            if truck[0] >= route[3]:
                # Mise à jour du tableau de résultat si la valeur est supérieure avec ce camion
                if result[budget - truck[1] + route[3]] < result[budget - truck[1]] + route[2]:
                    result[budget - truck[1] + route[3]] = result[budget - truck[1]] + route[2]
    # Retourne le profit maximum
    return max(result)


print(algo_glouton(trucks, trips, budget))




'''

def algo_knapsack(trucks, trips, budget):
    # Création de la matrice des profits pour les objets et les poids du sac à dos
    n = len(trucks)
    m = budget + 1
    profits = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if j >= trucks[i][1]:
                profits[i][j] = trucks[i][0]
            if i > 0:
                profits[i][j] = max(profits[i][j], profits[i-1][j])
            if j > 0 and i > 0:
                remaining_budget = j - trucks[i][1]
                if remaining_budget > 0:
                    profits[i][j] = max(profits[i][j], profits[i-1][remaining_budget] + trucks[i][0])
    
    # Attribution des camions aux trajets à l'aide de la matrice des profits
    assignments = []
    i = n - 1
    j = budget
    while i >= 0 and j >= 0:
        if i == 0:
            if profits[i][j] > 0:
                assigned_truck = trucks[i]
                assigned_trip = trips[0]
                assignments.append((assigned_truck, assigned_trip))
                print(assignments)
            break
        if profits[i][j] > profits[i-1][j]:
            assigned_truck = trucks[i]
            assigned_trip = None
            for trip in trips:
                if assigned_truck[0] >= trip[3] and trip not in [a[1] for a in assignments]:
                    if not assigned_trip or trip[2] > assigned_trip[2]:
                        assigned_trip = trip
            if assigned_trip:
                assignments.append((assigned_truck, assigned_trip))
                print(assignments)
                j -= assigned_truck[1]
            else:
                i -= 1
        else:
            i -= 1
    
    return assignments
'''
