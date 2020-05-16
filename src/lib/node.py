class Node:
    def __init__(self, id=None):
        self.id = id
        self.neighbors = []

    def add_neighbor(self, neighbor, cost):
        """
            neighbor: Node
            cost: cost to "travel" to neighbor
        """
        node = (neighbor, cost)
        self.neighbors.append(node)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        # It may not be a good implementation. However, it is only for testing.
        return self.id

    def __lt__(self, other):
        return self.id < other.id
