def max_cost(start, goal):
    reachable = frozenset([start])
    goal = frozenset([goal])
    max_cost = 0
    while not goal.issubset(reachable):
        new_reachable = reachable.union([neighbor for neighbor, _ in start.neighbors])
        if new_reachable == reachable:
            return float("inf")
        reachable = new_reachable
        max_cost += 1
    return max_cost
