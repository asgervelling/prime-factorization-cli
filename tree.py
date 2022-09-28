from anytree import Node, RenderTree

a = Node(1920)

b_leaf = Node(2, parent=a)
c = Node(960, parent=a)

d_leaf = Node(2, parent=c)
e = Node(480, parent=c)

def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def pf(n: int) -> Node:
    # primes = [i for i in range(n) if is_prime(i)]
    p = 2
    while n >= p * p:
        if n % p == 0:
            print(f'{p} * ({n} % {p})')
            n = n / p
        else:
            p += 1
    print(f'== {n}')


pf(256)
pf(257)




""" for pre, fill, node in RenderTree(a):
    print("%s%s" % (pre, node.name)) """