from graphviz import Digraph
import random

def MergeSort(arr, depth=0, tree=None, parent_node=None):
    """MergeSort implementation with recursion tree tracking."""
    if tree is None:
        tree = Digraph(comment='MergeSort Recursion Tree')
    
    # Create a unique node ID for the current call
    node_id = f"MergeSort_{id(arr)}_{depth}"
    tree.node(node_id, label=f"MergeSort({arr})")
    
    # Connect to the parent node (if exists)
    if parent_node is not None:
        tree.edge(parent_node, node_id)
    
    # Base case: If the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr, tree
    
    # Recursive case: Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the left and right halves
    left_sorted, tree = MergeSort(left_half, depth + 1, tree, node_id)
    right_sorted, tree = MergeSort(right_half, depth + 1, tree, node_id)
    
    # Merge the sorted halves
    merged_arr = Merge(left_sorted, right_sorted, depth + 1, tree, node_id)
    
    return merged_arr, tree

def Merge(left, right, depth, tree, parent_node):
    """Merge two sorted arrays into one sorted array."""
    merged = []
    i = j = 0
    
    # Create a unique node ID for the Merge call
    node_id = f"Merge_{id(left)}_{id(right)}_{depth}"
    tree.node(node_id, label=f"Merge({left}, {right})")
    
    # Connect to the parent node
    if parent_node is not None:
        tree.edge(parent_node, node_id)
    
    # Merge the two arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged
    
# Generate a random array of n elements
n = 8
arr = random.sample(range(1, 100), n)
print("Input Array:", arr)

# Run MergeSort and generate the recursion tree
sorted_arr, tree = MergeSort(arr)
print("Sorted Array:", sorted_arr)

# Save and render the recursion tree
tree.render('mergesort_recursion_tree', format='png', cleanup=True)
print("Recursion tree saved as 'mergesort_recursion_tree.png'")
