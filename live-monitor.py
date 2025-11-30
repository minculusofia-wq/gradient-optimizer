#!/usr/bin/env python3
import requests
import time
import os
import subprocess
from datetime import datetime

def check_parallax_process():
    """Vérifie si Parallax tourne"""
    try:
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        return 'parallax' in result.stdout.lower()
    except:
        return False

def get_parallax_metrics():
    """Essaie de récupérer les vraies métriques Parallax"""
    try:
        # Essayer l'endpoint métriques
        response = requests.get("http://localhost:8080/metrics", timeout=2)
        if response.status_code == 200:
            return parse_real_metrics(response.text)
    except:
        pass
    
    # Fallback: métriques simulées mais réalistes
    return get_realistic_metrics()

def parse_real_metrics(metrics_text):
    """Parse les vraies métriques Parallax"""
    # Cette fonction devra être adaptée selon le format réel
    lines = metrics_text.split('\n')
    metrics = {
        'uptime': 0,
        'gpu_hours': 0,
        'bandwidth_gb': 0,
        'status': '🟢 FARMING RÉEL',
        'type': 'VRAIES MÉTRIQUES'
    }
    
    for line in lines:
        if 'uptime' in line.lower():
            try:
                metrics['uptime'] = float(line.split()[-1])
            except:
                pass
        elif 'bandwidth' in line.lower():
            try:
                bytes_val = float(line.split()[-1])
                metrics['bandwidth_gb'] = bytes_val / (1024**3)
            except:
                pass
    
    return metrics

def get_realistic_metrics():
    """Métriques réalistes basées sur le temps d'exécution"""
    if not hasattr(get_realistic_metrics, 'start_time'):
        get_realistic_metrics.start_time = time.time()
    
    uptime = (time.time() - get_realistic_metrics.start_time) / 3600
    
    if check_parallax_process():
        status = "🟢 PARALLAX ACTIF"
        gpu_hours = uptime * 0.8
        bandwidth = uptime * 45
    else:
        status = "🟡 PARALLAX ARRÊTÉ"
        gpu_hours = 0
        bandwidth = 0
    
    return {
        'uptime': uptime,
        'gpu_hours': gpu_hours,
        'bandwidth_gb': bandwidth,
        'status': status,
        'type': 'SIMULATION RÉALISTE'
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

# Monitoring en temps réel
try:
    print("🚀 GRADIENT LIVE MONITOR - PARALLAX ACTIF")
    print("==========================================")
    
    iteration = 0
    while True:
        os.system('clear')
        
        print("🍎 GRADIENT OPTIMIZER - FARMING LIVE")
        print("=" * 50)
        print(f"⏰ {datetime.now().strftime('%H:%M:%S')}")
        print(f"👛 Wallet: 8HZpe8...fEibx")
        print()
        
        metrics = get_parallax_metrics()
        rewards = calculate_rewards(metrics)
        
        print("📊 STATUT DU FARMING:")
        print(f"   🎯 Type:        {metrics['type']}")
        print(f"   📈 Status:      {metrics['status']}")
        print(f"   🕒 Uptime:      {metrics['uptime']:>7.1f} h")
        print(f"   🎮 GPU Hours:   {metrics['gpu_hours']:>7.1f} h")
        print(f"   🌐 Bandwidth:   {metrics['bandwidth_gb']:>7.1f} GB")
        
        print()
        print("💰 REWARDS ACUMULÉS:")
        print(f"   💎 Total GRAD:  {rewards['total_grad']:>8} GRAD")
        print(f"   🖥️  GPU:         {rewards['gpu_rewards']:>8} GRAD")
        print(f"   📡 Bandwidth:   {rewards['bandwidth_rewards']:>8} GRAD")
        print(f"   ⏰ Uptime:      {rewards['uptime_rewards']:>8} GRAD")
        
        print()
        
        # Progression
        progress = min(100, (rewards['total_grad'] / 10) * 100)
        bar = "█" * int(progress/2.5) + "░" * (40 - int(progress/2.5))
        print(f"📈 Progression: [{bar}] {progress:.1f}%")
        
        print()
        print("💡 CONSEILS:")
        if not check_parallax_process():
            print("   🚀 Pour démarrer: ./farm-parallax.sh")
        else:
            print("   ✅ Parallax tourne - farming en cours!")
        
        print(f"⏳ Mise à jour dans 10s... (Ctrl+C pour quitter)")
        
        iteration += 1
        time.sleep(10)

except KeyboardInterrupt:
    print("\n🎯 RÉSUMÉ DE SESSION:")
    print(f"   🕒 Temps total: {metrics['uptime']:.1f}h")
    print(f"   💰 Gains: {rewards['total_grad']} GRAD")
    print("   🚀 Pour relancer: ./farm-parallax.sh")
