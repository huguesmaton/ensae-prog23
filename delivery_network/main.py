from graph import Graph, graph_from_file, kruskal


data_path = "input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)

g = graph_from_file("input/network.04.in")
print(g.graph)
print(g.graph[1][1][2])