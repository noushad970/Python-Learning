values = [True, False]
print("p\tq\tPVQ\tAddition")  # Fixed: print statement syntax

for p in values:
    for q in values:
        p_or_q = p or q
        addition = True if( p_or_q and p )else False  
        print(f"{p}\t{q}\t{p_or_q}\t{addition}")