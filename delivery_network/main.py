from graph import *


numero = 1
budget = 25*(10**9)
filename = "input/trucks." + str(numero) + ".in"
camions = trucks_from_file(filename)
trajets = routes_out(numero)


def algo_glouton(camions, trajets, budget):
    # Tri des camions par coût croissant et par puissance décroissante
    sorted_trucks = sorted(camions, key=lambda t: (t[1], -t[0]))
    print(sorted_trucks[:10])
    # Tri des trajets par profit décroissant
    sorted_trips = sorted(trajets, key=lambda t: t[2], reverse=True)
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

print(algo_glouton(camions, trajets, budget))