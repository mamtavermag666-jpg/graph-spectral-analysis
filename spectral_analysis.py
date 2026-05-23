import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Create graph
G = nx.cycle_graph(5)

# Adjacency matrix
A = nx.adjacency_matrix(G).toarray()

# Degree matrix
D = np.diag([d for n, d in G.degree()])

# Laplacian matrix
L = D - A

# Eigenvalues
eigenvalues = np.linalg.eigvals(L)

print("Adjacency Matrix:")
print(A)

print("\nLaplacian Matrix:")
print(L)

print("\nEigenvalues:")
print(eigenvalues)

# Draw graph
nx.draw(G, with_labels=True)
plt.show()