values=[True,False]
print("p\tq\t~p\t~q\tpVq\tDisjunctive Syllogism")

for p in  values:
    for q in values:
      not_p=not p
      not_q=not q
      p_or_q=p or q
      disjunctive_syllogism=True if (p_or_q and not p) else False
      print(f"{p}\t{q}\t{not p}\t{not q}\t{p_or_q}\t{disjunctive_syllogism}")
