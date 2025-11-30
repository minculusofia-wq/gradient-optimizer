#!/usr/bin/env python3
import time
import os
import sys
import psutil
import requests
from datetime import datetime

print("🔧 Initialisation du Gradient Monitor (Mode Réel)...")
time.sleep(1)

session_start = datetime.now()

def print_header():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;35m" + "="*60)
    print("           🚀 GRADIENT OPTIMIZER - LIVE DASHBOARD")
    print("="*60 + "\033[0m")
    print(f"⏰ Heure système: {datetime.now().strftime('%H:%M:%S')}")
    print(f"🕒 Session démarrée à: {session_start.strftime('%H:%M:%S')}")
    print()

def check_process_status():
    """Vérifie si le processus Parallax tourne"""
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # On cherche 'parallax' dans la ligne de commande
            if proc.info['cmdline'] and any('parallax' in arg for arg in proc.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def get_node_status():
    """Essaie de récupérer le statut via l'API locale"""
    try:
        # Le scheduler tourne par défaut sur 3001
        response = requests.get("http://localhost:3001", timeout=1)
        if response.status_code == 200:
            return "🟢 ONLINE (Scheduler)"
    except:
        pass
    
    # Si le scheduler ne répond pas, on vérifie juste le processus
    if check_process_status():
        return "🟡 RUNNING (Process detected)"
    
    return "🔴 OFFLINE"

def print_status(status):
    print("\033[1;36m📊 ÉTAT DU NŒUD:\033[0m")
    
    color = "\033[1;31m" # Rouge par défaut
    if "🟢" in status:
        color = "\033[1;32m"
    elif "🟡" in status:
        color = "\033[1;33m"
        
    print(f"   STATUS: {color}{status}\033[0m")
    print()
    
    if "OFFLINE" in status:
        print("\033[1;33m⚠️  Le nœud ne semble pas tourner.\033[0m")
        print("👉 Lance \033[1m./run-node.sh\033[0m dans un autre terminal.")
    elif "RUNNING" in status:
        print("\033[1;34mℹ️  Le processus tourne.\033[0m")
        print("🌍 Ouvre \033[1mhttp://localhost:3001\033[0m pour configurer.")
    else:
        print("\033[1;32m✅ Tout fonctionne correctement !\033[0m")
        print("💎 Farming potentiel en cours (selon activité réseau).")

# Boucle principale
try:
    while True:
        print_header()
        status = get_node_status()
        print_status(status)
        
        print("\n\033[1;90m⏳ Actualisation dans 5 secondes... (Ctrl+C pour quitter)\033[0m")
        time.sleep(5)
        
except KeyboardInterrupt:
    print("\n👋 Arrêt du monitor.")
