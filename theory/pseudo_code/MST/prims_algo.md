```
FUNCTION PrimMST(graph, start):
    MST ← ∅
    PriorityQueue PQ  // Min-heap
    INSERT (0, start) into PQ

    WHILE PQ is not empty:
        (weight, u) ← EXTRACT_MIN from PQ
        if u is already in MST:
            CONTINUE
        ADD u to MST

        for each (v, weight) in u's neighbors:
            if v is not in MST:
                INSERT (weight, v) into PQ
        endfor

    RETURN MST
end FUNCTION
```
