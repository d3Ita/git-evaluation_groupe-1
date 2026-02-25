#!/usr/bin/env python3
"""Generator - Génère des expressions arithmétiques aléatoires."""

import sys
import random


def main():
    #Erreur : Aucun argument 
    if len(sys.argv) < 2:
        print("Erreur : veuillez fournir le nombre d'expressions à générer.", file=sys.stderr)
        print("Utilisation : ./generator <nombre>", file=sys.stderr)
        sys.exit(1)

    #Erreur : Argument non entier 
    try:
        n = int(sys.argv[1])
    except ValueError:
        print(f'Erreur : "{sys.argv[1]}" n\'est pas un entier valide.', file=sys.stderr)
        sys.exit(1)

    operations = ['+', '-', '*', '/']

    for _ in range(n):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        op = random.choice(operations)
        print(f"{a}{op}{b}")


if __name__ == "__main__":
    main()
