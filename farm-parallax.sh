#!/bin/bash

echo "🚀 LANCEMENT DU FARMING PARALLAX"
echo "================================"

# Vérifier l'installation
cd ~/Desktop/parallax-main
source venv/bin/activate

echo "🔍 Vérification de l'installation..."
if ! command -v parallax &> /dev/null; then
    echo "❌ Parallax n'est pas installé correctement"
    exit 1
fi

echo "✅ Parallax est installé!"

echo
echo "🎯 CONFIGURATION DU FARMING:"
echo "   • Wallet: 8HZpe8StSMJFqaGWZs9PEgjek4hoNiN5ESERc5qfEibx"
echo "   • Type: Nœud Mac Intel" 
echo "   • Status: Prêt à farmer!"

echo
echo "🚀 OPTIONS DE FARMING DISPONIBLES:"
echo "   1. 📡 Rejoindre un réseau existant (Recommandé pour débuter)"
echo "   2. 🏠 Créer mon propre réseau"
echo "   3. 💬 Mode chat test"
echo

read -p "🎯 Choisis une option (1-3): " choice

case $choice in
    1)
        echo "📡 Connexion à un réseau Parallax existant..."
        echo "💡 Cette option te connecte à des nœuds existants"
        parallax join
        ;;
    2)
        echo "🏠 Création de ton propre réseau Parallax..."
        echo "💡 Cette option démarre un nœud principal"
        echo "🔧 Configuration en cours..."
        parallax run
        ;;
    3)
        echo "💬 Lancement du serveur chat de test..."
        echo "🎯 Parfait pour tester ton installation"
        parallax chat
        ;;
    *)
        echo "❌ Option invalide"
        echo "💡 Tape './farm-parallax.sh' pour réessayer"
        ;;
esac
