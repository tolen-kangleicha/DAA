```
FUNCTION KruskalMST(graph):
    SORT edges by weight  // O(E log E)
    CREATE disjoint sets for each vertex
    MST ← ∅  // Store selected edges

    for each edge (u, v) in sorted edges:
        if u and v are in different sets:
            ADD (u, v) to MST
            UNION(u, v)  // Merge sets
        endif
    endfor

    RETURN MST
end FUNCTION
```
