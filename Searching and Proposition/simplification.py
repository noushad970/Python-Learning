values=[True,False]
print("p\tq\tp^q\tSimplification")

for p in values:
    for q in values:
        p_and_q=p and q
        simplification=True if(p_and_q) else False
        print(f"{p}\t{q}\t{p_and_q}\t{simplification}")