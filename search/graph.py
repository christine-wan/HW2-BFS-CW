import networkx as nx
import queue

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        Method to perform breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # Check for invalid graph type
        if not isinstance(self.graph, nx.DiGraph):
            raise TypeError(f"Graph should be of type DiGraph, but it's {type(self.graph)}")

        # Check for empty graph
        if len(self.graph.nodes) == 0:
            return []

        # Check if the start node exists in the graph
        if start not in self.graph.nodes:
            raise ValueError(f"Start node {start} not found in the graph")

        # Check if the end node exists in the graph (if specified)
        if end is not None and end not in self.graph.nodes:
            raise ValueError(f"Ending node {end} not found in the graph")

        # Initialize the queue, visited list, and a dictionary to store the path and distance
        q = queue.Queue()
        visited = []
        distances = {start: (0, [start])}  # node: (distance, path)

        q.put(start)
        visited.append(start)

        while not q.empty():
            current_node = q.get()
            neighbors = list(self.graph.neighbors(current_node))

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    q.put(neighbor)

                    # Update the distance and path
                    new_path = distances[current_node][1] + [neighbor]
                    distances[neighbor] = (len(new_path) - 1, new_path)

                    # If end node is found, return the path
                    if end and neighbor == end:
                        return new_path

        # If end node was provided but no path was found
        if end:
            return None

        # Return the BFS traversal path (in the order the nodes were visited)
        return visited