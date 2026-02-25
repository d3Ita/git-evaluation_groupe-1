# Minitrice - Groupe 1

Calculatrice arithmétique élémentaire en ligne de commande, supportant les 4 opérations (+, -, *, /).

## Membres du groupe

- Adrien Lemettre
- Thibault Chaumont
- Yanis Vingadassamy
- Thomas Comorassamy

## Installation

### Prérequis

- Python 3.8 ou supérieur

Vérifier l'installation de Python :

```bash
python3 --version
```

Si Python n'est pas installé :

```bash
# Ubuntu / Debian
sudo apt update && sudo apt install python3
```

### Mise en place

Cloner le dépôt et rendre les programmes exécutables :

```bash
git clone https://github.com/<votre-compte>/git-evaluation_groupe-1.git
cd git-evaluation_groupe-1
chmod +x minitrice generator
```

## Exécution

### Mode interactif

```bash
$ ./minitrice
> 3+9
12
> 15/4
3.75
> 
Fin des calculs :)
$ echo $?
0
```

On quitte le mode interactif avec `Ctrl+D`.

### Via echo (pipe)

```bash
$ echo "3+12" | ./minitrice
15
$ echo $?
0
```

### Via cat (pipe)

```bash
$ cat good-expression.txt | ./minitrice
4
11
35
-4
12
90
4.0
8.0
10
4
$ echo $?
0
```

### Gestion d'erreurs

Erreur de syntaxe :

```bash
$ echo "3+*12" | ./minitrice
Erreur de syntaxe pour le calcul: "3+*12"
$ echo $?
1
```

Division par zéro :

```bash
$ echo "3/0" | ./minitrice
Division par zéro
$ echo $?
1
```

## Generator

### Utilisation

```bash
$ ./generator 5
342+718
91*3
500/25
87-42
123+456
```

### Composition avec minitrice

```bash
$ ./generator 5 | ./minitrice
```

### Gestion des erreurs

Le programme `generator` gère les erreurs suivantes :

1. **Argument manquant** : si aucun argument n'est fourni, un message d'erreur et l'utilisation correcte sont affichés.

```bash
$ ./generator
Erreur : veuillez fournir le nombre d'expressions à générer.
Utilisation : ./generator <nombre>
$ echo $?
1
```

2. **Argument non entier** : si l'argument n'est pas un nombre entier valide.

```bash
$ ./generator abc
Erreur : "abc" n'est pas un entier valide.
$ echo $?
1
```

3. **Nombre négatif ou nul** : si l'argument est inférieur ou égal à 0.

```bash
$ ./generator -5
Erreur : le nombre d'expressions doit être un entier positif.
$ echo $?
1
```

4. **Nombre trop grand** : si l'argument dépasse 1 000 000.

```bash
$ ./generator 9999999
Erreur : le nombre d'expressions demandé est trop grand (max: 1000000).
$ echo $?
1
```
