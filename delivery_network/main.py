from graph import Graph, graph_from_file, kruskal


data_path = "input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)

gtest = graph_from_file("input/network.05.in")
#print(gtest.graph)

print(g.graph)
print(g.graph[5])

#print(kruskal(gtest))
