from collections import Counter

from binarytree import Node

import latex
from tree import factor_tree


def count_exponents(node: Node) -> Counter:
    """Count the number of exponents in a prime factorization tree

    :param node:
        The root of the tree (or subtree) you would like to count
        the exponents of.

    :returns:
        A Counter, a dict-like object, where each key is a base
        and each value is the exponent to that base.
    """
    acc = []
    return _count_exp_recur(node, acc)


def _count_exp_recur(node: Node, acc: list) -> Counter:
    """Recursive helper function to count_exponents

    This is currently broken.
    For some reason it returns the term 4^1 when multiples of 2 are involved.
    f(64) returns 2^4 * 4^1, when it should return 2^5.
    Todo: fix
    """
    if node.left:
        _count_exp_recur(node.left, acc)
    if node.right:
        _count_exp_recur(node.right, acc)
    if node.value:
        if not node.left and not node.right:
            acc.append(node.value)
    c = Counter(acc)
    return c


def prime_factorization(n: int) -> str:
    """Prime factorization of n

    m = p1^a1 * p2^a2 * ... * pk^ak
    Ex.: pf(46) -> 2^1 * 23^1

    :returns:
        A LaTeX string containing the prime factorization of n
    """
    ftree = factor_tree(n)
    exponents = count_exponents(ftree)
    _latex = latex.render(exponents)
    return f'pf({n}) = {_latex}'