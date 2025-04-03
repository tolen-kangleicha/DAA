def longest_path_in_ordered_graph(G):
    n = len(G)  # number of nodes
    dp = [0] * n  # DP array to store the longest path length from each node
    
    # Traverse nodes from v_n-1 down to v_1
    for i in range(n - 2, -1, -1):  # starting from v_n-1 to v_1
        for j in range(i + 1, n):  # find the outgoing edges (i, j) with j > i
            if (i, j) in G:  # if there's an edge from v_i to v_j
                dp[i] = max(dp[i], 1 + dp[j])
    
    # dp[0] contains the length of the longest path starting at v1 and ending at vn
    return dp[0]
