import enum
import sys
from textwrap import dedent
from typing import Union

from binarytree import Node

from factorizations import prime_factorization
import latex
import plaintext
from tree import factor_tree


class FlagTypes(enum.Enum):
    TREE = ['-t', '--tree']
    HUMAN_READABLE = ['-h', '--human-readable']
    HELP = ['--help']

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Flag:
    def __init__(self, flag_type: FlagTypes) -> None:
        self.type = flag_type
        self.syntaxes = self.type.value

    @classmethod
    def tree(cls):
        return cls(FlagTypes.TREE)

    @classmethod
    def human_readable(cls):
        return cls(FlagTypes.HUMAN_READABLE)

    def __str__(self) -> str:
        return f'{self.type} - {self.syntaxes}'


def find_flags(args: list[str]) -> list[FlagTypes]:
    flags = []
    for flag_type in list(FlagTypes):
        flag_syntax = flag_type.value
        for arg in args:
            if arg in flag_syntax:
                flags.append(flag_type)
    return flags


def find_int(args: list[str]) -> Union[int, None]:
    for arg in args:
        if string_is_int(arg):
            return int(arg)
    return None


def string_is_int(s: str) -> bool:
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def render_tree(node: Node, human_readable=False):
    if human_readable:
        return plaintext.render(node)
    return latex.render(node)


def help():
    return dedent(
        '''
        Usage: python cli.py [OPTION]... [n]
        Do prime factorization on an integer n

            -t, --tree                  Show a prime factorization tree
            -h, --human-readable        Show as plaintext rather than LaTeX
    '''
    )


def cli():
    n = find_int(sys.argv)
    flags = find_flags(sys.argv)

    if FlagTypes.HELP in flags:
        print(help())
        return

    # Run
    is_hr = FlagTypes.HUMAN_READABLE in flags
    if FlagTypes.TREE in flags:
        node = factor_tree(n)
        print(render_tree(node, human_readable=is_hr))

    pf = prime_factorization(n, human_readable=is_hr)
    print(pf)


if __name__ == '__main__':
    cli()
