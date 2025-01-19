# write tests for bfs

import pytest
from search import graph
import networkx as nx
import random

def test_bfs_traversal():
    """
    Unit test for a breadth-first traversal

    Creates instance of Graph class using the 'tiny_network.adjlist' file and asserts that all nodes are being traversed
    (returns the right number of nodes, in the right order, etc.)

    """
    # Create an instance of Graph using tiny_network.adjlist
    tiny_network = graph.Graph("data/tiny_network.adjlist")

    # Obtain all nodes in the graph and pick a random node
    nodes_list = list(tiny_network.graph.nodes())
    random_node = random.choice(nodes_list)

    # Check that all nodes can be visited starting from a random node
    bfs_random = tiny_network.bfs(random_node)
    assert len(bfs_random) == len(nodes_list), "Not all nodes are connected or reachable."

    # Check the expected BFS order and node number starting from Lani Wu, as an example
    expected_order = list(nx.bfs_tree(tiny_network.graph, 'Lani Wu').nodes)
    order_lani = tiny_network.bfs('Lani Wu')
    assert order_lani == expected_order, f"Expected BFS order from 'Lani Wu': {expected_order}, but got: {order_lani}"
    assert len(order_lani) == len(expected_order), (
        f"Expected {len(expected_order)} nodes in BFS order, but got {len(order_lani)} nodes."
    )

    # ** Intentional Failing Test Case **
    # Use an invalid filename to create the graph and ensure an exception is raised
    with pytest.raises(FileNotFoundError):
        _ = graph.Graph("data/non_existent_file.adjlist")

def test_bfs():
    """
    Unit test for breadth-first search

    Generates an instance of a Graph class using the 'citation_network.adjlist' file and asserts that connected nodes return shortest paths between them
    Includes an additional test for nodes that are not connected which should return None
    """
    # Create an instance of Graph using citation_network.adjlist
    citation = graph.Graph("data/citation_network.adjlist")

    # Test correct implementation of search: shortest path
    # Using Marina Sirota --> Atul Butte as an example
    shortest_path = citation.bfs('Marina Sirota', 'Atul Butte')
    expected_shortest = nx.shortest_path(citation.graph, 'Marina Sirota', 'Atul Butte')
    assert len(shortest_path) == len(expected_shortest), (
        f"Expected shortest path from 'Marina Sirota' to 'Atul Butte': {expected_shortest}, " f"but got: {shortest_path}")

    # ** Edge Cases **
    # Test for a start node that does not exist (should raise ValueError)
    with pytest.raises(ValueError, match=r"Start node (.*) not found in the graph"):
        citation.bfs('Hello TAs', 'Atul Butte')

    # Test for a non-existent ending node (should raise ValueError)
    with pytest.raises(ValueError, match=r"Ending node (.*) not found in the graph"):
        citation.bfs('Tony Capra', 'Christine Wan')

    # Test for an empty graph (should return an empty list)
    empty = graph.Graph("data/empty.adjlist")
    assert empty.bfs('AnyNode') == []  # No nodes to visit in an empty graph

    # ** Additional Tests **
    # Test when nodes are not connected (should return None for an unreachable node)
    assert citation.bfs('Tony Capra', 'Alexander (Sandy) Johnson') is None

    # Testing that directionality matters
    # (there should be a path from Tony Capra to Jingjing Li, but not vice versa)
    assert citation.bfs('Tony Capra', 'Jingjing Li') is not None

