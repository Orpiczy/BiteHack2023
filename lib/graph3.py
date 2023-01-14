
import networkx as nx

nodes_nb = 9
office_graph_dict = {0: [1, 3],
                     1: [0, 2, 4],
                     2: [1, 5],
                     3: [0, 4, 6],
                     4: [1, 3, 5, 7],
                     5: [2, 4, 8],
                     6: [3, 7],
                     7: [4, 6, 8],
                     8: [5, 7]}

office_graph = nx.Graph(office_graph_dict)
# office_graph.add_nodes_from([i for i in range(nodes_nb)])

# for node, edges in office_graph_dict.items():
#     for edge in edges:
#         office_graph.add_edge(node, edge)

office_graph_eulerize = nx.eulerize(office_graph)
print(list(office_graph_eulerize.nodes))
print(nx.shortest_path(office_graph,0,8))
# print(nx.eulerian_path(office_graph,0))

obj = nx.eulerian_path(nx.eulerize(office_graph),5)
for i in obj:
    print(i[0])
    

    