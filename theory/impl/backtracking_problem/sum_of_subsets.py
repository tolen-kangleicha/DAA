from graphviz import Digraph

arr = [3, 2, 1]
target = 3

dot = Digraph(comment="Subset Sum Recursion Tree")
node_counter = 0
valid_subsets = []


def add_node(label):
    global node_counter
    node_id = f"n{node_counter}"
    dot.node(node_id, label)
    node_counter += 1
    return node_id


def build_tree(index, target, subset, parent=None):
    label = f"i={index}\ntarget={target}\n{subset}"
    current_node = add_node(label)

    if parent:
        dot.edge(parent, current_node)

    if target == 0:
        valid_subsets.append(subset)
        return
    if index >= len(arr) or target < 0:
        return

    # Include arr[index]
    build_tree(index + 1, target - arr[index], subset + [arr[index]], current_node)
    # Exclude arr[index]
    build_tree(index + 1, target, subset, current_node)


# Run with index starting at 0
build_tree(0, target, [])

# Save the tree image
dot.render("subset_sum_tree", format="png", cleanup=True)

# Print the valid subsets
print("Subsets that sum to", target, ":")
for s in valid_subsets:
    print(s)
