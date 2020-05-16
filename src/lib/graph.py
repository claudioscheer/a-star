class Graph:
    def __init__(self):
        self.nodes = []

    def add_nodes(self, nodes):
        """
            nodes: list of Node
        """
        self.nodes += nodes

    def add_node(self, node):
        """
            node: Node
        """
        self.add_nodes([node])

    def set_bidirectional_neighbor(self, node_1, node_2, cost):
        """
            node_1: Node
            node_2: Node
            cost: cost to "travel" from node_1 to node_2
        """
        node_1.add_neighbor(node_2, cost)
        node_2.add_neighbor(node_1, cost)
