# Cheatsheet - Graphs with NetworkX

### Importing the library

```python
import networkx as nx
```

### Creating a graph

```python
import networkx as nx

import numpy as np

G = nx.Graph()  # Undirected graph
G = nx.DiGraph()  # Directed graph
G = nx.MultiGraph()  # Undirected multigraph

G = nx.read_adjlist("/path/to/file", nodetype=int)  # Read a graph from a file (adjacency list)
G = nx.read_edgelist("/path/to/file", nodetype=int, data=[('weight', float)])  # Read a graph from a file (edge list)
G = nx.from_pandas_edgelist(df, 'n1', 'n2', edge_attr='weight')  # Read a graph from a pandas DataFrame

adj_matrix = np.array([[0, 1, 0],
                       [1, 0, 1],
                       [0, 1, 0]])
G = nx.Graph(adj_matrix)  # Create a graph from an adjacency matrix
```

### Nodes

```python
G.nodes  # Get the nodes of G
G.nodes(data=True)  # Get the nodes with data
G.nodes['A']  # Get the attributes of node 'A'

G.add_node('A')  # Add a node
G.add_nodes_from(['B', 'C', 'D'], bipartite=0)  # Bipartite graph
```

### Edges

```python
G.edges  # Get the edges of G
G.edges(data=True)  # Get the edges with data
G.edges['A', 'B']  # Get the attributes of edge ('A', 'B')

G.add_edge('A', 'B')
G.add_edges_from([('A', 'B'), ('A', 'C')])

G.add_edge('A', 'C', weight=6)  # Weighted edge
G.add_edge('A', 'B', sign='+')  # Signed edge
G.add_edge('A', 'B', relation='friend')  # Labeled edge

G.remove_edge('A', 'B')  # Remove an edge
```

### Distance

```python
nx.shortest_path(G, 'A', 'B')  # Shortest path between 'A' and 'B'
nx.shortest_path_length(G, 'A', 'B')  # Length of the shortest path between 'A' and 'B'
nx.shortest_path_length(G, 'A')  # Length of the shortest path from 'A' to all other nodes

nx.average_shortest_path_length(G)  # Average shortest path length
nx.eccentricity(G)  # Eccentricity of nodes (maximum distance to any other node)
nx.diameter(G)  # Diameter of G (maximum eccentricity)
nx.radius(G)  # Radius of G (minimum eccentricity)
nx.periphery(G)  # Periphery of G (nodes with eccentricity equal to the diameter)
nx.center(G)  # Center of G (nodes with eccentricity equal to the radius)

T = nx.bfs_tree(G, 'A')  # Breadth-first search tree
T.edges()  # Edges of the BFS tree
```

### Connectivity

```python
nx.is_connected(G)  # Check if G is connected
nx.is_strongly_connected(G)  # Check if G is strongly connected
nx.is_weakly_connected(G)  # Check if G is weakly connected
nx.number_connected_components(G)  # Number of connected components
nx.node_connected_component(G, 'A')  # Connected component of 'A'
nx.connected_components(G)  # Connected components
nx.strongly_connected_components(G)  # Strongly connected components
nx.weakly_connected_components(G)  # Weakly connected components
```

### Communities

```python
import community

partition = community.best_partition(G)  # Community detection
```

### Centrality

```python
import networkx as nx

nx.degree_centrality(G)  # Degree centrality (fraction of nodes connected to)
nx.in_degree_centrality(G)  # In-degree centrality
nx.out_degree_centrality(G)  # Out-degree centrality

btwnCent = nx.closeness_centrality(G, k=10)  # Closeness centrality. k is the maximum distance to consider
sorted(btwnCent.items(), key=lambda x: x[1], reverse=True)[0:5]  # Top 5 nodes by closeness centrality
btwnCent = nx.betweenness_centrality_subset(G, sources=['A', 'B'],
                                            targets=['X', 'Y'])  # Betweenness centrality between subsets of nodes
btwnCent_edge = nx.edge_betweenness_centrality(G)  # Edge betweenness centrality
btwnCent_edge = nx.edge_betweenness_centrality_subset(G, sources=['A', 'B'],
                                                      targets=['X', 'Y'])  # Edge betweenness subset

pagerank = nx.pagerank(G, alpha=0.9)  # PageRank centrality. Aplha is the damping factor
```

### Consistency

```python
import networkx as nx

nx.node_connectivity(G)  # Node connectivity (minimum number of nodes that must be removed to disconnect G)
nx.minimum_node_cut(G)  # Minimum node cut (set of nodes that disconnect G when removed)
nx.edge_connectivity(G)  # Edge connectivity (minimum number of edges that must be removed to disconnect G)
nx.minimum_edge_cut(G)  # Minimum edge cut (set of edges that disconnect G when removed)

nx.all_simple_paths(G, 'A', 'B')  # All simple paths between 'A' and 'B'
nx.node_connectivity(G, 'A', 'B')  # Node connectivity between 'A' and 'B'
nx.minimum_node_cut(G, 'A', 'B')  # Minimum node cut between 'A' and 'B'
nx.edge_connectivity(G, 'A', 'B')  # Edge connectivity between 'A' and 'B'
nx.minimum_edge_cut(G, 'A', 'B')  # Minimum edge cut between 'A' and 'B'
```

### Display graphs

```python
nx.draw_networkx(G1)
plt.show()
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=20, font_weight='bold')
```

### Bipartite graphs

```python
bipartite.is_bipartite(G)  # Check if G is bipartite  

bipartite.sets(G)  # Get the bipartite node sets of G

X = bipartite.set([1, 2, 3, 4])
bipartite.is_bipartite_node_set(G, X)  # Check if X is a bipartite node set

fans = set(['A', 'B', 'C', 'D'])
net_fans = bipartite.projected_graph(G, fans)  # Projected graph of fans

teams = set(['X', 'Y', 'Z'])
net_teams = bipartite.weighted_projected_graph(G, teams)  # Weighted projected graph of teams
```