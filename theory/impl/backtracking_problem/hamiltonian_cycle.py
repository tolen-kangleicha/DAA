# Number of vertices
n = 5

# Initialize graph as adjacency matrix
adj = [[0] * n for _ in range(n)]

# Example edges (undirected)
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


# Fill adjacency matrix
for u, v in edges:
    adj[u][v] = 1
    adj[v][u] = 1

x = [-1] * n  # solns
x[1] = 0  # Start at vertex 0


def is_safe(k, v):
    # Check if v is adjacent to previous vertex in path
    if adj[x[k - 1]][v] == 0:
        return False
    # Check if v is already in the path
    for j in range(1, k):
        if x[j] == v:
            return False
    return True


def HC(k):
    for v in range(1, n):  # Try all vertices except the starting one (0)
        if is_safe(k, v):
            x[k] = v
            if k == n - 1:
                if adj[x[k]][x[1]] == 1:  # Check for a cycle
                    print(x[1:n] + [x[1]])  # Print cycle
            else:
                HC(k + 1)
            x[k] = -1  # Backtrack


HC(2)
