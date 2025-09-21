values = [True, False]  # Changed to boolean values for clarity
print("P\tQ\tR\tP→Q\tQ→R\tP→R\tHypothetical Syllogism")

for p in values:
    for q in values:
        for r in values:
            p_implies_q = (not p) or q
            q_implies_r = (not q) or r 
            p_implies_r = (not p) or r 
            hs = True if (p_implies_q and q_implies_r and p_implies_r) else False
           
            print(f"{p}\t{q}\t{r}\t{p_implies_q}\t{q_implies_r}\t{p_implies_r}\t{hs}")
