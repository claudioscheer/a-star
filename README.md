## About

This is a vanilla implementation of the [A* (A-star)](https://en.wikipedia.org/wiki/A*_search_algorithm) algorithm.


## Heuristic

A* is guided by a heuristic. Therefore, in [`heuristic.py`](src/heuristic.py) I implemented the max-cost heuristic. Below is the heuristic mathematical formula.

$$
h^{max}(s,g)=\max_{g_i \in g}
\begin{cases}
0, & \text{if } g_i \in s\\
\min \{cost(a) + h^{max}(s,pre(a))\text{ | }a \in A \text{ and }g_i \in \text{eff}(a)\} & \text{otherwise}\\
\end{cases}
$$

## References

- [https://www.redblobgames.com/pathfinding/a-star/introduction.html](https://www.redblobgames.com/pathfinding/a-star/introduction.html)