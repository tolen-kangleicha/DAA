```
GreedyKnapsack(p,w,n,M)
begin
	// Initialize soln vector, array x[1..n] to 0’s. 
    // Sort the objects in the decreasing order of their profit/weight ratios 
    // such that (pi/wi) >= (pi+1/wi+1) for all 1<= i <n.   Ω(nlogn)    O(nlogn)
    Cu = M;					                                Ω(1)	    O(1)
    profit = 0;							                Ω(1)	    O(1)
    for i = 1 to n do						                Ω(1)	    O(n)
	    if w[i]<= Cu then					                Ω(1)	    O(n)
    		x[i] = 1;// put in the whole of object i	    		Ω(0)	    O(n)
    		profit = profit + p[i].x[i];			        	Ω(0)	    O(n)
    		Cu = Cu – w[i].x[i];				            	Ω(0)	    O(n)
    	else
    		x[i] = Cu/w[i];				                    	Ω(0)	    O(1)
    		profit = profit + p[i].x[i];			        	Ω(0)	    O(1)
    		Cu = 0;  //i.e., Cu = Cu - w[i].x[i];	        		Ω(0)	    O(1)
    		exit; //exit out of the for loop		        	Ω(0)	    O(1)
    	endif 
    end for 
end

```
