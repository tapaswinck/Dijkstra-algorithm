# Dijkstra-algorithm

# Dijkstra's Shortest Path Algorithm Implementation

## Overview

This Python script implements Dijkstra's algorithm for finding the shortest path between nodes in a weighted graph using the NetworkX library. The implementation provides a custom `shortest_path()` function that calculates the most efficient route between a starting and target node.

## Features

- Custom implementation of Dijkstra's algorithm
- Uses NetworkX for graph data structure
- Handles weighted graphs
- Returns the shortest path between two nodes

## Dependencies

- NetworkX
- Python's math module

## Algorithm Explanation

The `shortest_path()` function works by:
1. Initializing explored nodes and distance tracking
2. Iteratively exploring the graph to find the shortest route
3. Keeping track of node distances and predecessors
4. Constructing the shortest path from start to target node

## Usage Example

```python
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edge(0, 1, weight=5)
G.add_edge(1, 6, weight=100)
# ... (add more edges)

# Find shortest path from node 0 to node 6
shortest_route = shortest_path(G, 0, 6)
print(shortest_route)
```

## Key Functions

- `shortest_path(G, s, t)`: 
  - `G`: NetworkX graph
  - `s`: Starting node
  - `t`: Target node
  - Returns the shortest path from `s` to `t`

## Limitations

- Assumes non-negative edge weights
- Works with undirected graphs
- Prints "No possible path" if no route exists


## Author

Tapas
