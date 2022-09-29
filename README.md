# Prime factorization CLI
Do prime factorization for LaTeX and plaintext in your terminal.

```
$ python3 cli.py --help

Usage: python cli.py [OPTION]... [n]
Do prime factorization on an integer n

    -t, --tree                  Show a prime factorization tree
    -h, --human-readable        Show as plaintext rather than LaTeX

```

```
$ python cli.py 1030 -h
pf(1030) = 2¹ ⋅ 5¹ ⋅ 103¹
```

```
$ python cli.py 1030
pf(1030) = 2^1 \cdot 5^1 \cdot 103^1
```

```
$ python cli.py 1030 -h -t

  1030___
 /       \
2        515_
        /    \
       5     103

pf(1030) = 2¹ ⋅ 5¹ ⋅ 103¹
```