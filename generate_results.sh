#!/bin/bash
# Script pour générer les fichiers de résultats
# À exécuter depuis la racine du dépôt

mkdir -p results

# Vérifier que le dossier test existe
if [ ! -d "test" ]; then
    echo "Erreur : le dossier test/ n'existe pas."
    exit 1
fi

# Parcourir tous les fichiers .txt du dossier test
for f in test/*.txt; do
    if [ -f "$f" ]; then
        # Extraire le nom sans extension
        name=$(basename "$f" .txt)
        # Exécuter minitrice et stocker le résultat
        cat "$f" | ./minitrice > "results/${name}-result.txt"
        echo "Généré : results/${name}-result.txt"
    fi
done

echo "Tous les résultats ont été générés dans results/"
