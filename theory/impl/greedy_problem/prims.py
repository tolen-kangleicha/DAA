import heapq

def prim_mst(graph, V):
    min_heap = [(0, 0)]  # (weight, vertex)
    mst = []
    visited = set()

    while len(visited) < V:
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        mst.append((u, weight))

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))

    return mst

# Example Usage
V = 4
graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

mst = prim_mst(graph, V)
print("Minimum Spanning Tree (Prim's):", mst)
