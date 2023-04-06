from graph import *


numero = 1
budget = 25*(10**9)
filename = "input/trucks." + str(numero) + ".in"
trucks = trucks_from_file(filename)
trips = routes_out(numero)


def algo_glouton(trucks, trips, budget):
    # Tri des camions par coût croissant et par puissance décroissante
    sorted_trucks = sorted(trucks, key=lambda t: (t[1], -t[0]))
    print(sorted_trucks[:10])
    # Tri des trajets par profit décroissant
    sorted_trips = sorted(trips, key=lambda t: t[2], reverse=True)
    print(sorted_trips[:10])
    assignments = []
    total_profit = 0
    
    for trip in sorted_trips:
        # Recherche du camion le moins cher qui peut effectuer le trajet
        assigned_truck = None
        for truck in sorted_trucks:
            if truck[0] >= trip[3] and (total_profit + trip[2] - truck[1] <= budget):
                assigned_truck = truck
                break
        if assigned_truck:
            # Ajout de l'attribution à la liste des attributions
            assignments.append((assigned_truck, trip))
            # Mise à jour du profit total
            total_profit += trip[2] - assigned_truck[1]
            # Suppression des camions plus puissants pour éviter leur utilisation future
            sorted_trucks = [t for t in sorted_trucks if t[0] < assigned_truck[0]]
    
    return assignments

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

print(algo_knapsack(trucks, trips, budget))