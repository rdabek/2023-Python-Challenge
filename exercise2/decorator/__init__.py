def dec(ev1: float, ev2: float, sign: chr, func: callable) -> float:
    def addition(ev1: float, ev2: float, func: callable) -> float:
        return func(ev1+ev2)
    
    if sign is not '+' and sign is not '-':
        raise ValueError("Invalid character. Sign is '+' or '-'")
    if sign is '+':
        return addition(ev1, ev2, func)
    else:
        return addition(ev1, -ev2, func)

def reversecomp(l: list[callable], x: float) -> callable(float):
    def compose(f: callable(float), g: callable(float)) -> callable(float):
        return lambda x : f(g(x))
    
    lenList = len(l)
    retFunc = lambda x : l[lenList-1](x)
    for i in reversed(range(lenList - 1)):
        retFunc = compose(retFunc, l[i])
    
    return retFunc
