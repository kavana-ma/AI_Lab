import itertools

def evaluate(expr, model):
    """
    Replaces propositional symbols with their truth values from model
    and evaluates the expression.
    Supported operators:
      ~ : NOT
      ^ : AND
      v : OR
      ->: IMPLIES
      <->: BICONDITIONAL
    """
    for sym, val in model.items():
        expr = expr.replace(sym, str(val))
    
    expr = expr.replace("~", " not ")
    expr = expr.replace("^", " and ")
    expr = expr.replace("v", " or ")
    expr = expr.replace("->", " <= ")   # a -> b is equivalent to not a or b
    expr = expr.replace("<->", " == ")  # a <-> b is equivalent to (a and b) or (~a and ~b)
    
    return eval(expr)

def tt_entails(kb, query, symbols):
    """
    KB: knowledge base expression (string)
    query: query expression (string)
    symbols: list of all propositional symbols used
    """
    entails = True

    models = list(itertools.product([True, False], repeat=len(symbols)))

    print("Truth Table Evaluation:\n")
    header = " | ".join(symbols) + " | KB | Query | KB ⇒ Query"
    print(header)
    print("-" * len(header) * 2)

    for values in models:
        model = dict(zip(symbols, values))
        kb_val = evaluate(kb, model)
        query_val = evaluate(query, model)
        implication = (not kb_val) or query_val

        if kb_val and not query_val:
            entails = False

        row = " | ".join(['T' if v else 'F' for v in values])
        row += f" | {'T' if kb_val else 'F'}  | {'T' if query_val else 'F'}   | {'T' if implication else 'F'}"
        print(row)

    print("\nResult:")
    if entails:
        print("The Knowledge Base entails the Query (KB ⊨ Query)")
    else:
        print("The Knowledge Base does NOT entail the Query (KB ⊭ Query)")


kb = "(Q -> P) ^ (P -> ~Q) ^ (Q v R)"
symbols = ["P", "Q", "R"]

queries = ["R", "R -> P", "Q -> R"]

for query in queries:
    print(f"\nEvaluating Query: {query}\n")
    tt_entails(kb, query, symbols)
    print("\n" + "="*50 + "\n")

