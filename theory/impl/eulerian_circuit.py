# from collections import defaultdict


def find_eulerian_circuit(graph):
    circuit = []
    stack = []
    current = next(iter(graph))  # Start from any vertex
    stack.append(current)

    while stack:
        if graph[current]:
            stack.append(current)
            next_vertex = graph[current].pop()
            graph[next_vertex].remove(current)  # Remove both directions
            current = next_vertex
        else:
            circuit.append(current)
            current = stack.pop()

    return circuit[::-1]  # Reverse to get correct order


# Example graph as adjacency list
graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["A", "B", "C"],
}

circuit = find_eulerian_circuit(graph)
print("Eulerian Circuit:", circuit)
