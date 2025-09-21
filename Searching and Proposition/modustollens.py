p_sentence = input("Enter the value of p:")
q_sentence = input("Enter the value of q:")
values = [True, False]  # Changed to boolean values for clarity

print("\nModus Tollens Truth Table")
print(f"P: {p_sentence}")
print(f"Q: {q_sentence}")
print("-" * 50)
print("p\tq\t~p\t~q\tp->q\tModus Tollens")

for p in values:
    for q in values:
        not_p = not p
        not_q = not q
        implication = (not p) or q
        # Modus Tollens: If (p->q) and ~q, then ~p
        modus_tollens = True if implication and not_q else False
        
        print(f"{p}\t{q}\t{not_p}\t{not_q}\t{implication}\t{modus_tollens}")