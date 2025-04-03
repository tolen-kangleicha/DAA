procedure DANDC(p, q)
    global n, A(1:n)
    integer m, p, q     // 1 <= p <= q <= n
    
    if SMALL(p, q) then
        return G(p, q)
    else 
        m = DIVIDE(p, q)    //p <= m < q
        return COMBINE(DANDC(p, m), DANDC(m + 1, q))
    endif
end procedure
