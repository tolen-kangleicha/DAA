```
FUNCTION IntervalScheduling(intervals, n):
    SORT intervals by finish time in ascending order  // O(n log n)
    
    selected ← [first interval]
    last_finish_time ← finish time of first interval

    for i = 2 to n:
        if intervals[i].start >= last_finish_time:
            ADD intervals[i] to selected
            last_finish_time ← intervals[i].finish
        endif
    endfor

    RETURN selected
end FUNCTION
```
