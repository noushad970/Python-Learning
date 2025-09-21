values=[True,False]
print("p\tq\tr\tpVq\tnot_p^r\tqVr\tResolution")
for p in values:
    for q in values:
        for r in values:
            not_p= not p
            p_or_q=p or q
            not_p_and_r=not_p and r
            q_or_r=q or r
            resoluton=True if(p_or_q and not_p_and_r and q_or_r)else False
            print(f"{p}\t{q}\t{r}\t{p_or_q}\t{not_p_and_r}\t{q_or_r}\t{resoluton}")