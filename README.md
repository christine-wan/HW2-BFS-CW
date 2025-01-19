![BuildStatus](https://github.com/<christine-wan>/HW2-BFS-1/workflows/HW2-BFS/badge.svg?event=push)

# Assignment 2
Breadth-first search

# Assignment Overview
The purpose of this assignment is to get you comfortable working with graph structures and to implement a breadth-first search function to traverse the graph and find the shortest path between nodes.

# Breadth-First Search (BFS)
Breadth First Search (BFS) is a graph search algorithm that traverses through a graph - one layer at a time. This method utilizes a queue data structure, which follows a First In First Out (FIFO) order. As such, BFS visits vertices in the graph in the order of each vertex's distance from the source. 

The bfs function generated within this assignment conducts the following, taking in a graph, start node, and optional end node:

    * If no end node is provided, returns a list of nodes in order of breadth-first search traversal from the given start node
    * If an end node is provided and a path exists, returns a list of nodes in order of the shortest path to the end node
    * If an end node is provided and a path does not exist, returns None
    * Considers several edge cases, including: running bfs traversal on an empty graph, running bfs from a start node that does not exist in the graph, and running bfs search for an end node that does not exist in the graph


