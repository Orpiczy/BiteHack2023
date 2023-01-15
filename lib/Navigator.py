from Commander import Commander
import networkx as nx
office_graph_dict = {0: [1, 3],
                     1: [0, 2, 4],
                     2: [1, 5],
                     3: [0, 4, 6],
                     4: [1, 3, 5, 7],
                     5: [2, 4, 8],
                     6: [3, 7],
                     7: [4, 6, 8],
                     8: [5, 7]}

dist = 4
                          #x, y
office_graph_xy_pos = {0: [0     , 0],
                       1: [dist  , 0],
                       2: [2*dist, 0],
                       3: [0     , dist],
                       4: [dist  , dist],
                       5: [2*dist, dist],
                       6: [0     , 2*dist],
                       7: [dist  , 2*dist],
                       8: [2*dist, 2*dist]}





blocked_edges = [(0, 1), (1, 2)]
blocked_nodes = [9]

office_graph = nx.Graph(office_graph_dict)

# nav = Commander(office_graph)

# nav.search()

# position
#   0
# 3   1 
#   2
#

class Navigator:
    def __init__(self):
        self.current_orientation = 3
        self.current_node = 0      
        self.commander = Commander(office_graph, starting_node = self.current_node, detect_obstacle_callback=self.ride_and_return_true_if_obstacle_was_detected)
    
    def check_distance(self,next_node):
        delta_x = self.get_postion(next_node)[0] - self.get_postion(self.current_node)[0]
        delta_y = self.get_postion(next_node)[1] - self.get_postion(self.current_node)[1]
        return delta_x,delta_y
        
    def get_desired_orientation(self,delta_x,delta_y):
            
        desired_orientation = -1
        
        # delta == 0 means we don't need to change the orientation in that direction
        
        if delta_x > 0:
            desired_orientation = 1
        elif delta_x < 0:
            desired_orientation = 3
            
        if delta_y > 0:
            desired_orientation = 2
        elif delta_y < 0:
            desired_orientation = 0
            
        return desired_orientation

    def get_orientation_delta(self, current_orientation, desired_orientation):
        rotation = desired_orientation - current_orientation
        if rotation > 2:
            return -1 
        elif rotation < 2:
            return 1
        else:
            return rotation
        
        
    def get_postion(self,node):
        return office_graph_xy_pos[node]
    
    def ride_and_return_true_if_obstacle_was_detected(self,next_node):
        
        # TODO: implement riding function here, if obstacle was hit, 
        # return to previous node and return true from this function,
        # additionally update current orientation
        
        rotation, distance, desired_orientation = self.calculate_cmd(next_node)
        
        # was_obstacle_detected, orientation_at_cmd_end = riding(rotation, distance)
        
        was_obstacle_detected = (self.current_node, next_node) in blocked_edges
        
        if not was_obstacle_detected:
            self.current_node = next_node
            self.current_orientation = desired_orientation
        else:
            self.current_node = self.current_node
            # self.current_orientation = orientation_at_cmd_end
            
        return was_obstacle_detected
        
    
    def calculate_cmd(self,destination):
        delta_x, delta_y = self.check_distance(destination)
        desired_orientation = self.get_desired_orientation(delta_x, delta_y)
        orientation_delta = self.get_orientation_delta(self.current_orientation,desired_orientation)
        rotation = orientation_delta * 90
        distance = max(abs(delta_x),abs(delta_y))
        print("<<< CALCULATED CMD FOR LOWER LAYERS >>>")
        print("rotation = ",rotation,", distance = ",distance, ", destination = ",destination)
        
        return rotation, distance, desired_orientation
        
    def get_obstacles(self):
        raport = self.commander.search()
        return raport
    
    
nav = Navigator()
print(nav.get_obstacles())