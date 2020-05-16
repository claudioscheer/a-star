from lib import Graph, Node


def get_graph_1():
    graph = Graph()
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    graph.set_bidirectional_neighbor(node_1, node_2, 1)
    graph.set_bidirectional_neighbor(node_1, node_3, 1)
    graph.set_bidirectional_neighbor(node_3, node_2, 3)

    graph.add_nodes([node_1, node_2, node_3])

    return graph, node_3, node_2
