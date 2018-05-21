def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first(a, b):
        return a
    return pair(first)

def cdr(pair):
    def last(a, b):
        return b
    return pair(last)

print(car(cons(3, 4)), cdr(cons(3, 4)))
