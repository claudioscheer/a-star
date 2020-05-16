## About

This is a vanilla implementation of the [A* (A-star)](https://en.wikipedia.org/wiki/A*_search_algorithm) algorithm.


## Heuristic

A* is guided by a heuristic. Therefore, in [`heuristics.py`](src/heuristics.py) I implemented the max-cost heuristic. Below is the heuristic mathematical formula.

<img src="https://latex.codecogs.com/png.latex?h^{max}(s,g)=\max_{g_i%20\in%20g}\begin{cases}0,%20&%20\text{if%20}%20g_i%20\in%20s\\\min%20\{cost(a)%20+%20h^{max}(s,pre(a))\text{%20|%20}a%20\in%20A%20\text{%20and%20}g_i%20\in%20\text{eff}(a)\}%20&%20\text{otherwise}\\\end{cases}" />

## References

- [https://www.redblobgames.com/pathfinding/a-star/introduction.html](https://www.redblobgames.com/pathfinding/a-star/introduction.html)