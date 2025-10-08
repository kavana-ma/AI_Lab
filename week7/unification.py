def is_variable(x):
    return isinstance(x, str) and x.islower() 

def is_constant(x):
    return isinstance(x, str) and x[0].isupper()  

def occurs_check(var, expr, subst):
    """Check if var occurs in expr after applying current substitution"""
    if var == expr:
        return True
    elif isinstance(expr, list):
        return any(occurs_check(var, e, subst) for e in expr)
    elif expr in subst:
        return occurs_check(var, subst[expr], subst)
    return False

def unify(x, y, subst={}):
    """Main unification function"""
    if subst is None:
        return None
    elif x == y:
        return subst
    elif is_variable(x):
        return unify_var(x, y, subst)
    elif is_variable(y):
        return unify_var(y, x, subst)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        for xi, yi in zip(x, y):
            subst = unify(xi, yi, subst)
            if subst is None:
                return None
        return subst
    else:
        return None 

def unify_var(var, x, subst):
    if var in subst:
        return unify(subst[var], x, subst)
    elif is_variable(x) and x in subst:
        return unify(var, subst[x], subst)
    elif occurs_check(var, x, subst):
        return None  
    else:
        subst[var] = x
        return subst

# f(X, g(Y)) -> ['f', 'X', ['g', 'Y']]
expr1 = ['f', 'X', ['g', 'Y']]
expr2 = ['f', 'a', ['g', 'b']]

result = unify(expr1, expr2)
print("Unification Result:", result)


