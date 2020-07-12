"""
Implementation of Dijkstra Algorithm. Sorry but didn't work as expected
"""


class Graph:
    """
    class where our node connecting graph is defined
    """

    def __init__(self, node_matrix):
        self.node_matrix = node_matrix
        self.node_list = []

    def process_node_matrix(self):
        for i in range(0, len(self.node_matrix)):
            self.node_list.append(Node(i))

        for i in range(0, len(self.node_matrix)):
            for j in range(0, len(self.node_matrix[i])):
                if self.node_matrix[i][j] != 0:
                    self.node_list[i].add_neighbour(self.node_list[j], self.node_matrix[i][j])

    def print_node_list(self):
        for dude in self.node_list:
            print(dude.value)
            for guy in dude.list_of_neighbour_nodes:
                print(guy[0].value)
            print("\n")

    def find_shortest_path(self, start_index):
        start = self.node_list[start_index]

        queue = [start]
        visited = [None] * len(self.node_list)  # [None, None, None, None, None]
        visited[start.value] = 0  # [0, None, None, None, None]
        for current_node in queue:
            for node, distance in current_node.list_of_neighbour_nodes:  # [ (2, 5), (3, 15) ]
                # if node has not been visited
                if (visited[node.value] is None) or (visited[current_node.value] + distance < visited[node.value]):
                    # || node distance value is lower than current node distance in visited list
                    # then add to queue
                    queue.append(node)
                    # update visited with edge value
                    visited[node.value] = visited[current_node.value] + distance

        print(visited)


class Node:
    def __init__(self, value):
        self.value = value
        self.list_of_neighbour_nodes = []

    def add_neighbour(self, neighbour_node, distance):
        self.list_of_neighbour_nodes.append((neighbour_node, distance))


matrix = [
    [0, 5, 15, 0, 0],
    [5, 0, 6, 0, 0],
    [15, 6, 0, 2, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0]
]

graph_of_nodes = Graph(matrix)
graph_of_nodes.process_node_matrix()
graph_of_nodes.print_node_list()

graph_of_nodes.find_shortest_path(4)
