#!/usr/bin/env python3
import requests
import time
import os
import subprocess
from datetime import datetime

def check_parallax_running():
    """Vérifie si Parallax tourne sur le Mac"""
    try:
        # Essayer de détecter le processus Parallax
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if 'parallax' in result.stdout.lower():
            return True
        return False
    except:
        return False

def get_mac_metrics():
    """Récupère les métriques système du Mac"""
    try:
        # CPU usage
        cpu_result = subprocess.run(['top', '-l', '1'], capture_output=True, text=True)
        cpu_lines = cpu_result.stdout.split('\n')
        
        # Mémoire usage
        memory_result = subprocess.run(['vm_stat'], capture_output=True, text=True)
        
        # Simulation de métriques Parallax
        metrics = {
            'uptime': get_uptime(),
            'gpu_hours': get_gpu_usage(),
            'bandwidth_gb': get_bandwidth_estimate(),
            'status': '🟢 PARALLAX ACTIF' if check_parallax_running() else '🟡 PARALLAX ARRÊTÉ',
            'cpu_usage': extract_cpu_usage(cpu_lines),
            'memory_usage': extract_memory_usage(memory_result.stdout)
        }
        return metrics
    except Exception as e:
        print(f"❌ Erreur métriques: {e}")
        return get_fallback_metrics()

def get_uptime():
    """Calcule l'uptime depuis le démarrage du monitoring"""
    if not hasattr(get_uptime, 'start_time'):
        get_uptime.start_time = time.time()
    return (time.time() - get_uptime.start_time) / 3600  # en heures

def get_gpu_usage():
    """Estime l'usage GPU (simulation pour l'instant)"""
    uptime = get_uptime()
    return uptime * 0.7  # 70% d'utilisation GPU

def get_bandwidth_estimate():
    """Estime la bande passante utilisée"""
    uptime = get_uptime()
    return 40 * uptime + 10  # ~40GB/h + base

def extract_cpu_usage(cpu_lines):
    """Extrait l'usage CPU depuis la commande top"""
    for line in cpu_lines:
        if 'CPU usage' in line:
            return line.strip()
    return "CPU: N/A"

def extract_memory_usage(memory_output):
    """Extrait l'usage mémoire depuis vm_stat"""
    lines = memory_output.split('\n')
    if len(lines) > 1:
        return f"Memory: {lines[1].strip()}"
    return "Memory: N/A"

def get_fallback_metrics():
    """Métriques de fallback"""
    return {
        'uptime': 0.1,
        'gpu_hours': 0.07,
        'bandwidth_gb': 5.0,
        'status': '🟡 EN ATTENTE',
        'cpu_usage': 'CPU: En attente',
        'memory_usage': 'Memory: En attente'
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

# Monitoring principal
try:
    iteration = 0
    while True:
        os.system('clear')
        print("🍎 GRADIENT MONITOR - MACBOOK PRO")
        print("=" * 50)
        print(f"⏰ {datetime.now().strftime('%H:%M:%S')}")
        print()
        
        metrics = get_mac_metrics()
        rewards = calculate_rewards(metrics)
        
        print("📊 MÉTRIQUES SYSTÈME:")
        print(f"   🕒 Uptime:       {metrics['uptime']:>8.1f} h")
        print(f"   🎮 GPU Hours:    {metrics['gpu_hours']:>8.1f} h")
        print(f"   🌐 Bandwidth:    {metrics['bandwidth_gb']:>8.1f} GB")
        print(f"   📈 Status:       {metrics['status']}")
        print(f"   🔧 {metrics['cpu_usage']}")
        print(f"   💾 {metrics['memory_usage']}")
        
        print()
        print("💰 REWARDS ESTIMÉS:")
        print(f"   💎 Total GRAD:   {rewards['total_grad']:>8} GRAD")
        print(f"   🖥️  GPU:          {rewards['gpu_rewards']:>8} GRAD")
        print(f"   📡 Bandwidth:    {rewards['bandwidth_rewards']:>8} GRAD")
        print(f"   ⏰ Uptime:       {rewards['uptime_rewards']:>8} GRAD")
        
        print()
        
        # Messages d'info
        messages = [
            "💡 Pour lancer Parallax: ./deploy-mac.sh",
            "🚀 Parallax utilise MLX pour l'accélération Apple Silicon",
            "📈 Optimisé pour les GPU Apple M-series",
            "🌡️  Surveillance température et performance",
            "🎯 Objectif: Maximiser les rewards airdrop"
        ]
        
        print(f"💡 {messages[iteration % len(messages)]}")
        print()
        print("⏳ Mise à jour dans 15s... (Ctrl+C pour quitter)")
        
        iteration += 1
        time.sleep(15)

except KeyboardInterrupt:
    print("\n🛑 Monitoring arrêté")
    print("🚀 Pour installer Parallax: ./deploy-mac.sh")
    print("🌐 Interface web: http://localhost:8000")
