from graph import Graph, graph_from_file, kruskal


data_path = "input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)

gtest = graph_from_file("input/network.05.in")
print(gtest.graph)

gtestliste = []
for node in gtest.graph:
    for neighbor, weight, dist in gtest.graph[node]:
        if node < neighbor:  # Ajout des arêtes une seule fois pour éviter les doublons
            gtestliste.append((node, neighbor, weight))
print(gtestliste)



aretes = []
for node1 in gtest.graph:
    for node2, power_min, dist in gtest.graph[node1]:
        aretes.append((power_min, node1, node2))
aretes.sort()
print(aretes)

print(kruskal(gtest))

gg=Graph(range(1,12))
print(gg.graph)