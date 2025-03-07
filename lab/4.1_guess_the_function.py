from graphviz import Digraph

# Function to build the recursion tree
def build_tree(x, n, graph=None, parent_node=None):
    print(f"Guess({x}, {n})")

    if graph is None:
        graph = Digraph(comment='Recursion Tree')

    # Create a unique node ID
    node_id = f"{x}_{n}"

    # Add the current node to the graph
    graph.node(node_id, label=f"Guess({x}, {n})")

    # Connect to the parent node (if exists)
    if parent_node is not None:
        graph.edge(parent_node, node_id)

    if n == 1:
        return x, graph
    
    if n % 2 == 0:  # Even
        result, graph = build_tree(x + x, n // 2, graph, node_id)
        return result, graph
    else:  # Odd
        result, graph = build_tree(x + x, n // 2, graph, node_id)
        return x + result, graph
        
# Function to display the recursion tree
def draw_recursion_tree(x, n):
    result, graph = build_tree(x, n)
    print(f"Result: {result}")
    graph.render(f'recursion_tree_{x}_{n}', format='png', cleanup=True)
    print(f"Recursion tree saved as 'recursion_tree_{x}_{n}.png'\n")
    return graph

# Test cases
for x, n in [(3, 7), (5, 20), (6, 9)]:
    print(f"Execution of Guess({x}, {n}):") 
    draw_recursion_tree(x, n)
