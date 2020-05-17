from lib import Graph, Node


def get_graph_1():
    graph = Graph()
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)

    graph.set_bidirectional_neighbor(node_1, node_2, 1)
    graph.set_bidirectional_neighbor(node_1, node_3, 1)
    graph.set_bidirectional_neighbor(node_2, node_4, 1)
    graph.set_bidirectional_neighbor(node_3, node_4, 1)
    graph.set_bidirectional_neighbor(node_3, node_5, 1)
    graph.set_bidirectional_neighbor(node_5, node_6, 1)

    graph.add_nodes([node_1, node_2, node_3, node_4, node_5, node_6])

    return graph, node_1, node_6
