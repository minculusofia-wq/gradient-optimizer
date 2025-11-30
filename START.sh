#!/bin/bash

echo "#############################################"
echo "#   🚀 GRADIENT OPTIMIZER - LANCEUR AUTO   #"
echo "#############################################"
echo

# Couleurs pour le terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Fonction pour afficher des messages stylisés
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_gradient() {
    echo -e "${PURPLE}[GRADIENT]${NC} $1"
}

# Vérifier qu'on est dans le bon dossier
if [ ! -f "deploy.sh" ]; then
    print_error "Tu n'es pas dans le dossier gradient-optimizer!"
    echo "Ouvre le terminal et tape:"
    echo "cd ~/Desktop/gradient-optimizer"
    echo "puis: ./START.sh"
    exit 1
fi

print_gradient "Démarrage du Gradient Optimizer..."
echo

# Étape 1: Lancer le serveur web en arrière-plan
print_status "1. Lancement du serveur web sur http://localhost:8000"
python3 -m http.server 8000 > server.log 2>&1 &
SERVER_PID=$!
print_success "Serveur web lancé (PID: $SERVER_PID)"

# Étape 2: Ouvrir le navigateur automatiquement
print_status "2. Ouverture du navigateur..."
sleep 2
open http://localhost:8000/app.html
print_success "Navigateur ouvert"

# Étape 3: Lancer le monitoring
print_status "3. Lancement du monitoring en temps réel..."
echo "============================================="
print_gradient "📊 MONITORING GRADIENT - TEMPS RÉEL"
print_gradient "Appuie sur Ctrl+C pour arrêter le monitoring"
echo "============================================="
echo

# Lance le monitoring Python
python3 monitor.py

# Si on arrive ici, le monitoring s'est arrêté
echo
print_warning "Monitoring arrêté"
print_status "Le serveur web tourne toujours sur http://localhost:8000"
print_status "Pour tout arrêter, ferme ce terminal ou tape: kill $SERVER_PID"
