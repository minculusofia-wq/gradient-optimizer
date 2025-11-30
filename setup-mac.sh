#!/bin/bash

echo "🔧 Initialisation de l'environnement Gradient pour Mac..."

# Vérification de Python 3.11+
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé. Installe-le via https://www.python.org/downloads/"
    exit 1
fi

# Création du venv
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activation
source venv/bin/activate

# Détection de l'architecture
ARCH=$(uname -m)
echo "🖥️  Architecture détectée : $ARCH"

# Installation des dépendances
echo "⬇️ Installation de Parallax..."
cd parallax

if [ "$ARCH" = "arm64" ]; then
    echo "✅ Apple Silicon détecté. Installation complète avec support GPU (MLX)..."
    pip install -e '.[mac]'
else
    echo "⚠️  Intel Mac détecté. Installation en mode SCHEDULER uniquement."
    echo "ℹ️  Installation de PyTorch (requis)..."
    pip install torch torchvision torchaudio "numpy<2"
    echo "ℹ️  Installation de Parallax (sans MLX)..."
    pip install -e .
fi

echo "✅ Installation terminée !"
echo "👉 Lance ./run-node.sh pour démarrer."
