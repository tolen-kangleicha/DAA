from graphviz import Digraph

graph = Digraph(format='png')  # Graphviz Directed Graph

def opt(i, M, p, w, parent):
    global count, graph
    count += 1  # Count function calls
    node_id = f"({i+1},{M})"  # Unique node name

    if parent:  # Add edge in Graphviz graph
        graph.edge(parent, node_id)

    if M < 0:  # Invalid state (exceeded capacity)
        return float('-inf')
    if i < 0:  # No items left
        return 0

    # Recursive cases
    val_1 = opt(i - 1, M, p, w, node_id)  # Exclude item i
    val_2 = p[i] + opt(i - 1, M - w[i], p, w, node_id)  # Include item i

    return max(val_1, val_2)

# Function to solve a problem instance
def solve_knapsack(p, w, M, problem_name):
    global count, graph
    count = 0  # Reset call counter
    graph.clear()  # Reset Graphviz graph

    max_profit = opt(len(p) - 1, M, p, w, None)  # Start recursion

    # Render the recursion tree
    graph.render(problem_name, view=True)  # Saves as {problem_name}.png and opens it

    return max_profit, count  # Return results

if __name__ == "__main__":
    print("\n===== Test Case: 01 =====")
    p1 = [1, 2, 5]
    w1 = [2, 3, 4]
    M1 = 6
    print(f"p = {p1} \nw = {w1} \nM = {M1}")
    profit1, calls1 = solve_knapsack(p1, w1, M1, "knapsack_tree_1")
    print(f"\nMax Profit: {profit1} \nNo. of Calls: {calls1}")

    print("\n\n===== Test Case: 02 =====")
    p2 = [10, 5, 20, 30]
    w2 = [3, 2, 3, 4]
    M2 = 9
    print(f"p = {p2} \nw = {w2} \nM = {M2}")
    profit2, calls2 = solve_knapsack(p2, w2, M2, "knapsack_tree_2")
    print(f"\nMax Profit: {profit2} \nNo. of Calls: {calls2}")
