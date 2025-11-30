#!/bin/bash

echo "🔧 CORRECTION DES DÉPENDANCES PARALLAX"
echo "======================================"

cd ~/Desktop/parallax-main
source venv/bin/activate

echo "📦 Installation des dépendances manquantes..."

# MLX ne fonctionne pas sur Intel, installons les alternatives
echo "🔧 Installation des packages compatibles Intel..."
pip uninstall -y mlx-core mlx-lm 2>/dev/null || true

# Réinstaller avec les bonnes dépendances
echo "📦 Réinstallation des dépendances GPU..."
pip install --force-reinstall "numpy<2"  # Compatibilité NumPy
pip install "torch>=2.0.0" --index-url https://download.pytorch.org/whl/cpu
pip install "transformers>=4.57.1"
pip install "sglang[all]==0.5.5" --no-deps
pip install --no-deps "lattica==1.0.14"

echo "🔍 Vérification des installations..."
python3 -c "
try:
    import torch
    print('✅ PyTorch:', torch.__version__)
except Exception as e:
    print('❌ PyTorch:', e)

try:
    import transformers
    print('✅ Transformers:', transformers.__version__)
except Exception as e:
    print('❌ Transformers:', e)

try:
    import sglang
    print('✅ SGLang: OK')
except Exception as e:
    print('❌ SGLang:', e)
"

echo
echo "🚀 ESSAI AVEC LE MODE CHAT (plus simple):"
parallax chat --help || echo "❌ Le mode chat ne marche pas non plus"

echo
echo "💡 CONSEIL: Parallax semble optimisé pour Apple Silicon/GPU NVIDIA"
echo "   Sur Mac Intel, on pourrait essayer les autres composants Gradient!"
