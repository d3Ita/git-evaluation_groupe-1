#!/usr/bin/env python3
"""Generator - Génère des expressions arithmétiques aléatoires."""

import sys
import random


def main():
    n = int(sys.argv[1])

    operations = ['+', '-', '*', '/']

    for _ in range(n):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        op = random.choice(operations)
        print(f"{a}{op}{b}")


if __name__ == "__main__":
    main()
