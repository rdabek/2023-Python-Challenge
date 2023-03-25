def count(f: callable):
    n = 0
    def inner(x):
        nonlocal n
        n += 1
        return (n, f(x))

    return inner