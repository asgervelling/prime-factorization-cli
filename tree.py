from binarytree import Node


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


def factor_tree(n):
    node = Node(n)

    for i in range(2, int(n / 2)):
        if n % i != 0:
            continue

        node.left = factor_tree(i)
        node.right = factor_tree(int(n / i))
        return node

    val = node.value
    if val > 2 and val % 2 == 0:
        # Dirty fix for an odd problem. f(8) returns 2^1 * 4^1 otherwise
        node = factor_tree(int(val / 2))
    return node
