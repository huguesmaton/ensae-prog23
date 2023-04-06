from graph import Graph, graph_from_file, kruskal


data_path = "input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)

g = graph_from_file("input/network.05.in")
print(g.graph)
print(g.get_path_with_power(1, 3, 2))