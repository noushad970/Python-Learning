
p_sentence = "It is raining"
q_sentence = "the ground is wet"

values = [True, False]

print("p\tq\tp->q\tModus Ponens")
# ...existing code...

for p in values:
    for q in values:
        implication=(not p) or q
        modus_ponnens=None
        if p and implication:
            modus_ponnens=True
        else:
            modus_ponnens=False
        print(f"{p}\t{q}\t{implication}\t{modus_ponnens}")
