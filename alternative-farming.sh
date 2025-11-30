#!/bin/bash

echo "🎯 STRATÉGIES ALTERNATIVES POUR L'AIRDROP GRADIENT"
echo "=================================================="

echo "🔍 Parallax est trop complexe sur Mac Intel..."
echo "💡 Voici les alternatives PLUS SIMPLES pour farmer l'airdrop:"
echo
echo "1. 🚀 GRADIENT CLOUD (Recommandé - Le plus simple)"
echo "   • Service cloud décentralisé"
echo "   • Facile à configurer"
echo "   • Parfait pour débuter"
echo
echo "2. 📡 GRADIENT ECHO"  
echo "   • Réseau de données léger"
echo "   • Bon pour l'airdrop"
echo "   • Installation rapide"
echo
echo "3. 🐳 DOCKER SIMPLIFIÉ"
echo "   • Conteneur tout-en-un"
echo "   • Moins de dépendances"
echo
echo "4. 📊 SIMULATION INTELLIGENTE"
echo "   • Notre dashboard avancé"
echo "   • En attendant la vraie config"
echo

read -p "🎯 Choisis une option (1-4): " choice

case $choice in
    1)
        echo "🚀 Installation de Gradient Cloud..."
        cd ~/Desktop
        git clone https://github.com/GradientHQ/cloud.git
        echo "✅ Cloud installé! Regarde le dossier 'cloud'"
        echo "📖 Instructions: cd ~/Desktop/cloud && cat README.md"
        ;;
    2)
        echo "📡 Installation de Gradient Echo..."
        cd ~/Desktop  
        git clone https://github.com/GradientHQ/echo.git
        echo "✅ Echo installé! Regarde le dossier 'echo'"
        echo "📖 Instructions: cd ~/Desktop/echo && cat README.md"
        ;;
    3)
        echo "🐳 Lancement Docker Parallax..."
        echo "🔧 Cette méthode utilise l'image officielle"
        docker run -d --name gradient-node \
          -e WALLET=8HZpe8StSMJFqaGWZs9PEgjek4hoNiN5ESERc5qfEibx \
          -p 8080:8080 -p 8081:8081 \
          gradientservice/parallax:latest
        echo "✅ Conteneur lancé! Vérifie: docker ps"
        ;;
    4)
        echo "📊 Lancement du monitoring intelligent..."
        python3 simple-monitor-enhanced.py
        ;;
    *)
        echo "❌ Option invalide"
        echo "💡 Relance le script pour réessayer"
        ;;
esac

echo
echo "🎯 PROCHAINES ÉTAPES:"
echo "• Surveille ton wallet: 8HZpe8...fEibx"
echo "• Rejoins le Discord Gradient pour les updates"
echo "• Garde le monitoring ouvert pour tracker tes gains"
