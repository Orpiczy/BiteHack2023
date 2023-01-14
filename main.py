import random
import networkx as nx

office_graph_dict = {0: [1, 3],
                     1: [0, 2, 4],
                     2: [1, 5],
                     3: [0, 4, 6],
                     4: [1, 3, 5, 7],
                     5: [2, 4, 8],
                     6: [3, 7],
                     7: [4, 6, 8],
                     8: [5, 7],
                    #  9: [],
}
office_graph = nx.Graph(office_graph_dict)
office_graph_eulerize = nx.eulerize(office_graph)

# a  = nx.shortest_path(office_graph_eulerize,0,9)


# print([edges for edges in nx.eulerian_path(office_graph_eulerize,5)])
print(office_graph.edges)
test_tuple = (1,2)
office_graph.remove_edge(0,1)
print(office_graph.edges)
