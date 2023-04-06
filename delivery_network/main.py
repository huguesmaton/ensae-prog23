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

def algo_glouton(trucks, trips, budget):

    trucks = camions_utiles(trucks)
    # trier les camions par puissance décroissante
    trucks = sorted(trucks, key=lambda t: t[0], reverse=True)
    
    # trier les routes par profit décroissant
    trips = sorted(trips, key=lambda r: r[2], reverse=True)
    
    assigned_trucks = {}
    assigned_budget = 0
    
    for route in trips: #On parcourt les trajet et pour chaque trajet, on choisit le meilleur camion
        start, end, profit, power_min = route
        
        for truck in trucks:
            power, cost = truck
            
            if power >= power_min and assigned_budget + cost <= budget:
                assigned_trucks[(start, end)] = truck
                assigned_budget += cost
                break
        
    return assigned_trucks



def algo_knapsack(camion_list, trajet_list, budget):

    camion_list = camions_utiles(trucks)
    # Tri des trajets par profit décroissant
    trajet_list = sorted(trajet_list, key=lambda t: t[2], reverse=True)
    # Initialisation de la matrice de programmation dynamique
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(trajet_list) + 1)]
    # Remplissage de la matrice de programmation dynamique
    for i in range(1, len(trajet_list) + 1):
        for j in range(budget + 1):
            if camion_list:
                if trajet_list[i-1][3] <= camion_list[0][0]:
                    # Le camion le plus puissant peut satisfaire les besoins du trajet
                    dp[i][j] = max(dp[i-1][j], trajet_list[i-1][2] + dp[i-1][j-camion_list[0][1]])
                else:
                    # Le camion le plus puissant ne peut pas satisfaire les besoins du trajet
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    # Récupération de la solution optimale
    i = len(trajet_list)
    j = budget
    trucks_assigned = []
    while i > 0 and j >= 0:
        if dp[i][j] != dp[i-1][j]:
            # Le trajet i a été satisfait
            trucks_assigned.append((i-1, camion_list[0]))
            j -= camion_list[0][1]
            camion_list.pop(0)
        i -= 1
    trucks_assigned.reverse()
    return trucks_assigned


print(algo_knapsack(trucks, trips, budget))




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
