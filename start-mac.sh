#!/bin/bash

echo "🍎 LANCEUR GRADIENT OPTIMIZER - MAC"
echo "==================================="

# Donner les permissions
chmod +x deploy-mac.sh
chmod +x mac-monitor.py

echo "🚀 Options disponibles:"
echo "   1. 🔧 Installer Parallax"
echo "   2. 📊 Lancer le monitoring Mac" 
echo "   3. 🌐 Ouvrir l'interface web"
echo "   4. ❌ Tout arrêter"
echo

read -p "🎯 Choisis une option (1-4): " choice

case $choice in
    1)
        echo "🔧 Installation de Parallax..."
        ./deploy-mac.sh
        ;;
    2)
        echo "📊 Lancement du monitoring Mac..."
        python3 mac-monitor.py
        ;;
    3)
        echo "🌐 Lancement du serveur web..."
        python3 -m http.server 8000 &
        sleep 2
        open http://localhost:8000/app.html
        echo "✅ Interface ouverte: http://localhost:8000/app.html"
        ;;
    4)
        echo "🛑 Arrêt des services..."
        pkill -f "python3 -m http.server"
        echo "✅ Services arrêtés"
        ;;
    *)
        echo "❌ Option invalide"
        ;;
esac
