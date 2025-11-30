#!/bin/bash

echo "🍎 DÉPLOIEMENT PARALLAX POUR MAC"
echo "================================"

# Vérifier que c'est un Mac
if [[ $(uname) != "Darwin" ]]; then
    echo "❌ Ce script est pour macOS seulement"
    exit 1
fi

# Détection Apple Silicon ou Intel
ARCH=$(uname -m)
if [[ $ARCH == "arm64" ]]; then
    echo "✅ Mac Apple Silicon (M1/M2/M3) détecté"
    CHIP="apple_silicon"
else
    echo "✅ Mac Intel détecté"
    CHIP="intel"
fi

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    echo "📦 Installation: brew install python@3.11"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $PYTHON_VERSION détecté"

# Vérifier la version Python
if [[ $(python3 -c "import sys; print(sys.version_info >= (3, 11))") != "True" ]]; then
    echo "❌ Python 3.11 ou supérieur requis"
    echo "📦 Mise à jour: brew upgrade python@3.11"
    exit 1
fi

# Demander le wallet
echo
read -p "💰 Entre ton adresse wallet Solana: " WALLET_ADDRESS
if [ -z "$WALLET_ADDRESS" ]; then
    echo "❌ Wallet requis pour les rewards!"
    exit 1
fi

echo "🚀 Démarrage de l'installation Parallax..."

# Aller dans le dossier Parallax
cd ~/Desktop/parallax-main

# Créer l'environnement virtuel
echo "📦 Création de l'environnement virtuel..."
python3 -m venv ./venv
source ./venv/bin/activate

# Installation Parallax pour Mac
echo "🔧 Installation de Parallax avec support Mac..."
pip install --upgrade pip

if [[ $CHIP == "apple_silicon" ]]; then
    echo "🔧 Installation avec accélération Apple Silicon..."
    pip install -e '.[mac]'
else
    echo "🔧 Installation version standard Mac Intel..."
    pip install -e .
fi

echo "✅ Installation terminée!"

# Créer un script de lancement facile
cat > ~/Desktop/gradient-optimizer/start-parallax.sh << LAUNCHER
#!/bin/bash
cd ~/Desktop/parallax-main
source venv/bin/activate
echo "🚀 Parallax prêt! Tape: parallax --help"
LAUNCHER

chmod +x ~/Desktop/gradient-optimizer/start-parallax.sh

echo
echo "🎯 CONFIGURATION TERMINÉE!"
echo "   • Wallet: $WALLET_ADDRESS"
echo "   • Architecture: $ARCH"
echo "   • Environnement: venv activé"
echo "   • Parallax: Installé avec support Mac"
echo
echo "🚀 POUR LANCER PARALLAX:"
echo "   cd ~/Desktop/gradient-optimizer"
echo "   ./start-parallax.sh"
echo
echo "📊 POUR MONITORER:"
echo "   ./start-mac.sh (choisir option 2)"
echo
echo "💡 TEST RAPIDE:"
echo "   Tape cette commande pour vérifier l'installation:"
echo "   cd ~/Desktop/parallax-main && source venv/bin/activate && parallax --help"
