from queue import PriorityQueue
from graph_tests import get_graph_1
from heuristics import max_cost


def get_backward_path(current, came_from, reverse=False):
    path = []
    while came_from[current]:
        path.append(current)
        current = came_from[current]
    path.append(current)
    if reverse:
        path.reverse()
    return path


def a_star(graph, start_node, goal_node, heuristic):
    queue = PriorityQueue()
    queue.put(start_node, 0)
    # Keep track from where the Node came from.
    came_from = {}
    came_from[start_node] = None
    # Keep track of cost movements from the start location.
    cost_so_far = {}
    cost_so_far[start_node] = 0

    while not queue.empty():
        current = queue.get()
        if current == goal_node:
            return get_backward_path(current, came_from, True)

        for neighbor, cost in current.neighbors:
            new_cost = cost_so_far[current] + cost
            # If the cost is not yet tracked or is lower than previous one, use the new cost.
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal_node)
                queue.put(neighbor, priority)
                came_from[neighbor] = current


graph, start_node, goal_node = get_graph_1()
path = a_star(graph, start_node, goal_node, max_cost)
print(f"Start node: {start_node.id}. Goal node: {goal_node.id}")
print("-" * 5, end="")
print("Solution plan", end="")
print("-" * 5)
for x in path:
    print(x.id)
