#!/bin/bash

# Activation de l'environnement
source venv/bin/activate

echo "🚀 Lancement du nœud Gradient Parallax..."
echo "ℹ️  Si c'est la première fois, assure-toi d'avoir lancé ./setup-mac.sh avant."

# Vérification si un scheduler est spécifié
if [ -z "$1" ]; then
    echo "🌐 Mode Scheduler (Nœud Principal)..."
    echo "Ouvre http://localhost:3001 pour configurer ton cluster."
    parallax run
else
    echo "🔗 Connexion au Scheduler $1..."
    parallax join -s "$1"
fi
