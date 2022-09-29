from collections import Counter
from dataclasses import replace
from typing import Union

from binarytree import Node
from binarytree.exceptions import NodeValueError

from tree import factor_tree


def render(data) -> str:
    """Creates LaTeX based on a data structure

    :param data:
        See _render_counter(data) and _render_tree(data)

    :returns:
        The expression as LaTeX
    """
    if isinstance(data, (Counter, dict)):
        return _render_counter(data)
    if isinstance(data, Node):
        return _render_tree(data)
    if isinstance(data, list):
        _latex = [render(i) for i in data]
        return ''.join(_latex)


def _render_counter(data: Union[Counter, dict]) -> str:
    """Creates LaTeX based on a prime factorization (or just a dict)

    :param data:
        A Counter or dict where each key is a base
        and each value is the exponent to that base.

    :returns:
        The expression as LaTeX
    """
    latex = ''
    for base, exp in data.items():
        latex += f'{base}^{exp} \cdot '

    # Remove the last ' * '
    return latex[:-7]


def _render_tree(data: Node) -> str:
    ftree = str(factor_tree(data.value))
    return ftree \
        .replace('\\', '\setminus') \
        .replace(' ', '\ ') \
        .replace('_', '\ ') \
        .replace('\n', '    \\\\\n')
