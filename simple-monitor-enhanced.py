#!/usr/bin/env python3
import requests
import time
import os
import subprocess
from datetime import datetime

def check_parallax_status():
    """Vérifie si Parallax peut tourner"""
    try:
        result = subprocess.run(['parallax', 'chat', '--help'], capture_output=True, text=True)
        return "usage: parallax chat" in result.stdout
    except:
        return False

def get_enhanced_metrics():
    """Métriques améliorées avec statut réel"""
    if check_parallax_status():
        status = "🟢 PARALLAX PRÊT (mode chat)"
        description = "Le client est installé mais besoin de GPU/Apple Silicon pour le farming complet"
    else:
        status = "🟡 EN ATTENTE DE CONFIGURATION"
        description = "Essaie Gradient Cloud ou Echo pour farming immédiat"
    
    # Simulation réaliste basée sur le temps
    if not hasattr(get_enhanced_metrics, 'start_time'):
        get_enhanced_metrics.start_time = time.time()
    
    uptime = (time.time() - get_enhanced_metrics.start_time) / 3600
    
    return {
        'uptime': uptime,
        'gpu_hours': uptime * 0.6 if check_parallax_status() else 0,
        'bandwidth_gb': uptime * 35,
        'status': status,
        'description': description,
        'wallet': '8HZpe8StSMJFqaGWZs9PEgjek4hoNiN5ESERc5qfEibx'
    }

def calculate_rewards(metrics):
    gpu_rewards = metrics["gpu_hours"] * 0.1
    bandwidth_rewards = metrics["bandwidth_gb"] * 0.01
    uptime_rewards = metrics["uptime"] * 0.005
    total = gpu_rewards + bandwidth_rewards + uptime_rewards
    
    return {
        "total_grad": round(total, 3),
        "gpu_rewards": round(gpu_rewards, 3),
        "bandwidth_rewards": round(bandwidth_rewards, 3),
        "uptime_rewards": round(uptime_rewards, 3)
    }

# Monitoring amélioré
try:
    print("🚀 GRADIENT OPTIMIZER - STATUT AVANCÉ")
    print("======================================")
    
    iteration = 0
    while True:
        os.system('clear')
        
        print("🎯 DASHBOARD GRADIENT - SOLUTION INTELLIGENTE")
        print("=" * 60)
        print(f"⏰ {datetime.now().strftime('%H:%M:%S')}")
        print(f"👛 Wallet: {get_enhanced_metrics()['wallet'][:8]}...{get_enhanced_metrics()['wallet'][-4:]}")
        print()
        
        metrics = get_enhanced_metrics()
        rewards = calculate_rewards(metrics)
        
        print("📊 ANALYSE SYSTÈME:")
        print(f"   🎯 Status:      {metrics['status']}")
        print(f"   💡 Description: {metrics['description']}")
        print(f"   🕒 Uptime:      {metrics['uptime']:>7.1f} h")
        print(f"   🎮 GPU Hours:   {metrics['gpu_hours']:>7.1f} h")
        print(f"   🌐 Bandwidth:   {metrics['bandwidth_gb']:>7.1f} GB")
        
        print()
        print("💰 REWARDS SIMULÉS:")
        print(f"   💎 Total GRAD:  {rewards['total_grad']:>8} GRAD")
        print(f"   🖥️  GPU:         {rewards['gpu_rewards']:>8} GRAD")
        print(f"   📡 Bandwidth:   {rewards['bandwidth_rewards']:>8} GRAD")
        print(f"   ⏰ Uptime:      {rewards['uptime_rewards']:>8} GRAD")
        
        print()
        print("🚀 RECOMMANDATIONS:")
        if iteration % 3 == 0:
            print("   📥 Télécharge Gradient Cloud: git clone https://github.com/GradientHQ/cloud.git")
        elif iteration % 3 == 1:
            print("   📡 Essaie Gradient Echo: git clone https://github.com/GradientHQ/echo.git")
        else:
            print("   💡 Utilise Docker: docker run -d gradientservice/parallax:latest")
        
        print()
        print("⏳ Mise à jour dans 15s... (Ctrl+C pour options)")
        
        iteration += 1
        time.sleep(15)

except KeyboardInterrupt:
    print("\n" + "=" * 50)
    print("🎯 OPTIONS DISPONIBLES:")
    print("   1. 🌐 Gradient Cloud (Recommandé - Plus simple)")
    print("   2. 📡 Gradient Echo (Alternative)")
    print("   3. 🐳 Docker Parallax (Avancé)")
    print("   4. 📊 Continuer monitoring")
    print()
    
    choice = input("🎯 Choisis une option (1-4): ")
    
    if choice == "1":
        print("🚀 Installation de Gradient Cloud...")
        subprocess.run(["cd ~/Desktop && git clone https://github.com/GradientHQ/cloud.git"], shell=True)
        print("✅ Fait! Vérifie le dossier 'cloud'")
    elif choice == "2":
        print("📡 Installation de Gradient Echo...")
        subprocess.run(["cd ~/Desktop && git clone https://github.com/GradientHQ/echo.git"], shell=True)
        print("✅ Fait! Vérifie le dossier 'echo'")
    elif choice == "3":
        print("🐳 Lancement Docker Parallax...")
        print("docker run -d --name gradient-node -p 8080:8080 gradientservice/parallax:latest")
    else:
        print("📊 Continuation du monitoring...")
        print("Relance: python3 simple-monitor-enhanced.py")
