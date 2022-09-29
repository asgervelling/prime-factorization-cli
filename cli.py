import sys

from binarytree import Node

from factorizations import prime_factorization
import latex


def cli():
    n = int(sys.argv[1])
    tree = False
    if len(sys.argv) > 2:
        flag = sys.argv[2]
        if flag == '-t' or flag == '--tree':
            tree = True

    pf = prime_factorization(n)
    if tree:
        print(latex.render(Node(int(n))))
    print(pf)


if __name__ == '__main__':
    # sys.stdout.write(str(factor_tree(None, int(sys.argn[1]))))
    cli()