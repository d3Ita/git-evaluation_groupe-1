#!/usr/bin/env python3
"""Generator - Génère des expressions arithmétiques aléatoires."""

import sys
import random


def main():
    #Gestion erreur : pas d'argument
    if len(sys.argv) < 2:
        print("Erreur : veuillez fournir le nombre d'expressions à générer.", file=sys.stderr)
        print("Utilisation : ./generator <nombre>", file=sys.stderr)
        sys.exit(1)

    #Gestion erreur : argument non entier
    try:
        n = int(sys.argv[1])
    except ValueError:
        print(f'Erreur : "{sys.argv[1]}" n\'est pas un entier valide.', file=sys.stderr)
        sys.exit(1)

    #Gestion erreur : nombre négatif ou nul 
    if n <= 0:
        print("Erreur : le nombre d'expressions doit être un entier positif.", file=sys.stderr)
        sys.exit(1)

    #Gestion erreur : nombre beaucoup trop grand
    if n > 1000000:
        print("Erreur : le nombre d'expressions demandé est trop grand (max: 1000000).", file=sys.stderr)
        sys.exit(1)

    operations = ['+', '-', '*', '/']

    for _ in range(n):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        op = random.choice(operations)
        print(f"{a}{op}{b}")


if __name__ == "__main__":
    main()
