#!/bin/bash

echo "🔧 INSTALLATION DE PYTORCH POUR MAC INTEL"
echo "=========================================="

cd ~/Desktop/parallax-main
source venv/bin/activate

echo "📦 Installation de PyTorch pour Mac Intel..."
pip install torch torchvision torchaudio

echo "🔍 Vérification de l'installation..."
python3 -c "import torch; print(f'✅ PyTorch version: {torch.__version__}'); print(f'✅ CUDA disponible: {torch.cuda.is_available()}')"

echo
echo "🚀 RÉESSAYE LE FARMING MAINTENANT:"
echo "./farm-parallax.sh"
