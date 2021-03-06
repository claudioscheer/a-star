from lib import Graph, Node


def get_graph_1():
    graph = Graph()
    node_a = Node(1)
    node_b = Node(2)
    node_c = Node(3)
    node_d = Node(4)
    node_e = Node(5)

    graph.set_bidirectional_neighbor(node_a, node_b, 40)
    graph.set_bidirectional_neighbor(node_b, node_e, 20)

    graph.set_bidirectional_neighbor(node_a, node_c, 30)
    graph.set_bidirectional_neighbor(node_c, node_d, 10)
    graph.set_bidirectional_neighbor(node_d, node_e, 30)

    graph.add_nodes([node_a, node_b, node_c, node_d, node_e])

    return graph, node_a, node_e
