#!/bin/bash

echo "🎉 Bienvenue dans le Gradient Optimizer!"
echo "🌈 Let's farm this airdrop!"

# MODIFIE TON WALLET ICI!
WALLET="met_ton_wallet_ici"
NODE_NAME="gradient-macbook"

echo "💰 Wallet: $WALLET"
echo "🏷️ Nom du nœud: $NODE_NAME"

# Installation Docker si pas déjà fait
if ! command -v docker &> /dev/null; then
    echo "📦 Installation de Docker..."
    brew install docker
fi

# Clone Parallax depuis ton dossier existant
echo "📥 Copie de Parallax..."
cd ~/Desktop
cp -r parallax-main ~/Desktop/gradient-optimizer/parallax
cd ~/Desktop/gradient-optimizer/parallax

# Build et lance le nœud
echo "🚀 Lancement du nœud Gradient..."
docker build -t gradient-node .
docker run -d \
  --name $NODE_NAME \
  -p 8080:8080 \
  -p 8081:8081 \
  -e WALLET=$WALLET \
  gradient-node

echo "✅ Félicitations! Ton nœud est en ligne!"
echo "📊 Métriques: http://localhost:8080/metrics"
echo "💎 Tu farmes des GRAD maintenant!"
