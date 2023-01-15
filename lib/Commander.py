import time
import networkx as nx
import random

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

blocked_edges = [(0, 1), (1, 2), (3, 4),(7,8),(8,7)]
blocked_nodes = [9]

office_graph = nx.Graph(office_graph_dict)

class Commander:

    def __init__(self, graph, starting_node, detect_obstacle_callback):

        self.graph = graph
        self.map = nx.eulerize(graph)

        self.reset_visited()

        self.current_node = starting_node
        self.main_path = [edges for edges in nx.eulerian_path(
            self.map, self.current_node)]

        first_edge = self.main_path[0]
        self.next_node = first_edge[1]

        self.blocked_edges = []
        self.isolated_nodes = []
        
        self.detect_obstacle_callback = detect_obstacle_callback

    def search(self):

        self.reset_visited()
        self.print_status()
        print("PATH >>> ", self.main_path)
        while not self.check_if_all_edges_and_nodes_are_visited():

            is_obstacle_in_our_way = self.detect_obstacle(self.next_node)

            if not is_obstacle_in_our_way:

                self.print_status()
                self.update_visited(self.current_node, self.next_node)

                # self.send_cmd(self.next_node)
                self.current_node = self.next_node

                print("Popping  from main path : ", self.main_path.pop(0))
                if not self.check_if_all_edges_and_nodes_are_visited():
                    next_edge = self.main_path[0]
                    self.next_node = next_edge[1]

            else:

                self.remove_edge((self.current_node, self.next_node))
                self.go_around()

        self.prepare_results()
        self.print_summary()
        
        return self.get_search_summary()

    def go_around(self):

        print("<<< OBSTACLE >>> going around")
        while self.current_node != self.next_node:

            try:
                auxilary_path = nx.shortest_path(
                    self.map, self.current_node, self.next_node)

            except nx.NetworkXError:

                # next node is isolated
                self.isolated_nodes.append(self.next_node)
                self.remove_node(self.next_node)

                first_edge = self.main_path[0]
                self.next_node = first_edge[1]
                return

            is_obstacle_in_our_way = self.detect_obstacle(auxilary_path[1])

            if not is_obstacle_in_our_way:

                auxilary_path.pop(0)  # gets rid of current node from path

                dest_node = auxilary_path[0]
                # self.send_cmd(dest_node)
                self.current_node = dest_node

            else:
                self.remove_edge((self.current_node, auxilary_path[1]))

            self.print_status()

        self.update_visited(self.current_node, self.next_node)

        print("Popping  from main path : ", self.main_path.pop(0))
        next_edge = self.main_path[0]
        self.next_node = next_edge[1]
        print("Finished rerouting")

    def detect_obstacle(self, next_node):
        # return random.uniform(0, 1) > 1.1
        # return (self.current_node, next_node) in blocked_edges
        return self.detect_obstacle_callback(next_node)

    def remove_node(self, node_to_remove):
        self.graph.remove_node(node_to_remove)
        self.map = nx.eulerize(self.graph)

    def remove_edge(self, blocked_edge):
        print("Removing edge ", blocked_edge)
        self.blocked_edges.append(blocked_edge)

        try:
            self.graph.remove_edge(blocked_edge[0], blocked_edge[1])
        except:
            print("INFO >>> removing not existing edge, it was propably removed during rerouting procedure = ", blocked_edge)

        self.map = nx.eulerize(self.graph)

        self.visited_edges.pop((blocked_edge[0], blocked_edge[1]), None)
        self.visited_edges.pop((blocked_edge[1], blocked_edge[0]), None)

    def update_visited(self, start_node, end_node):
        self.visited_edges[(start_node, end_node)] = True
        self.visited_edges[(end_node, start_node)] = True
        self.visited_nodes[end_node] = True

    def reset_visited(self):
        self.visited_nodes = {node: False for node in self.graph.nodes}
        self.visited_edges = {edge: False for edge in self.graph.edges}

    def check_if_all_edges_and_nodes_are_visited(self):
        return all(self.visited_nodes.values()) and all(self.visited_edges.values())

    # def send_cmd(self, destination):
    #     print("<<< CMD >>>")
    #     print("destination : ", destination)
    

    def print_status(self, verbose=False, debug_run=False):
        if not debug_run:
            return

        print("<<SYSTEM STATUS>>")
        print("Current node : ", self.current_node,
              ", Next node : ", self.next_node)

        if verbose:
            print("Visited nodes : ", [
                  node for node, status in self.visited_nodes.items() if status])
            print("NOT Visited nodes : ", [
                  node for node, status in self.visited_nodes.items() if not status])
            print("Visited edges : ", [
                  edge for edge, status in self.visited_edges.items() if status])
            print("NOT Visited edges : ", [
                  edge for edge, status in self.visited_edges.items() if not status])

    def prepare_results(self):
        self.blocked_edges = set(self.blocked_edges)
        self.isolated_nodes = set(self.isolated_nodes)
    
    def get_search_summary(self):
        return {"blocked_edges": self.blocked_edges,
                "isolated_nodes": self.isolated_nodes}
        
    def print_summary(self):
        print("\n\n<<< FINAL RESULTS >>>")
        print("< OBSTACLES >")
        print("blocked edges: ", self.blocked_edges)
        print("isolated nodes: ", self.isolated_nodes)


# nav = Commander(office_graph)
# # try:
# nav.search()
# except Exception as e:
#     print("Error: ", e)
#     nav.print_status(verbose=True,debug_run=True)
