# 🚀 Gradient Optimizer - Parallax Node Runner

Un outil simple et optimisé pour exécuter un nœud Gradient Parallax sur macOS. Ce projet vous permet de participer au réseau Gradient et de préparer le farming de tokens.

## 📋 Table des matières

- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Structure du projet](#-structure-du-projet)
- [Monitoring](#-monitoring)
- [Farming](#-farming)
- [Dépannage](#-dépannage)
- [Sécurité](#-sécurité)
- [Contribution](#-contribution)
- [Licence](#-licence)

## ✨ Fonctionnalités

- ✅ Installation automatisée du nœud Parallax
- ✅ Scripts de lancement simplifiés (double-clic)
- ✅ Monitoring en temps réel de l'état du nœud
- ✅ Interface web pour visualiser l'activité
- ✅ Environnement virtuel Python isolé
- ✅ Support complet macOS (Intel & Apple Silicon)
- ✅ Gestion automatique des dépendances

## 🔧 Prérequis

- **macOS** (version 10.15 ou supérieure)
- **Python 3.8+** (généralement préinstallé sur macOS)
- **Homebrew** (recommandé pour installer les dépendances)
- **Connexion Internet** stable

## 📦 Installation

### Méthode 1 : Installation rapide (recommandée)

1. **Clonez ou téléchargez ce dépôt** :
   ```bash
   git clone https://github.com/minculusofia-wq/gradient-optimizer.git
   cd gradient-optimizer
   ```

2. **Lancez le script d'installation** :
   ```bash
   ./setup-mac.sh
   ```

   Ce script va :
   - Créer un environnement virtuel Python
   - Installer toutes les dépendances nécessaires
   - Configurer le nœud Parallax
   - Générer votre clé P2P unique

3. **Attendez la fin de l'installation** (peut prendre 5-10 minutes)

### Méthode 2 : Installation manuelle

Si vous préférez installer manuellement :

```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate

# Installer les dépendances
pip install --upgrade pip
pip install -r parallax/requirements.txt

# Installer PyTorch (si nécessaire)
./install-torch.sh
```

## 🎮 Utilisation

### Lancer le nœud

**Méthode simple (double-clic)** :
- Double-cliquez sur `LANCER_LE_NOEUD.command`

**Méthode Terminal** :
```bash
./start-mac.sh
```

Le nœud démarre et lance :
- Le **Scheduler** (orchestrateur de tâches)
- Le **Nœud Parallax** (participant au réseau)
- L'**interface web** accessible sur `http://localhost:3001`

### Arrêter le nœud

Appuyez sur `Ctrl+C` dans le terminal où le nœud est en cours d'exécution.

## 📊 Monitoring

### Surveillance en temps réel

**Méthode simple (double-clic)** :
- Double-cliquez sur `LANCER_LE_MONITEUR.command`

**Méthode Terminal** :
```bash
./run-monitor.sh
```

Le moniteur affiche :
- ✅ État du nœud (actif/inactif)
- 📡 Connexions P2P
- 🔄 Tâches en cours
- 📈 Statistiques de performance
- ⏱️ Uptime

### Interface web

Ouvrez votre navigateur et accédez à :
```
http://localhost:3001
```

Vous pouvez également consulter `LANCER.html` pour une interface de monitoring locale.

## 🌾 Farming

### Participation passive

Pour l'instant, le farming est **passif** :
1. Gardez votre nœud en ligne le plus longtemps possible
2. Participez aux tâches du réseau Gradient
3. Accumulez du temps d'activité (uptime)

### Lier votre wallet (à venir)

Gradient annoncera bientôt la possibilité de lier votre wallet pour recevoir des récompenses. Surveillez :
- [Site officiel Gradient](https://gradient.network)
- [Twitter Gradient](https://twitter.com/gradientnetwork)
- [Discord Gradient](https://discord.gg/gradient)

### Maximiser vos gains

- ⏰ **Uptime** : Gardez le nœud en ligne 24/7 si possible
- 🔌 **Stabilité** : Assurez une connexion Internet stable
- 🔐 **Sécurité** : Sauvegardez votre fichier `p2p.key`

## 📁 Structure du projet

```
gradient-optimizer/
├── README.md                        # Ce fichier
├── INSTRUCTIONS.txt                 # Instructions en français
├── LANCER_LE_NOEUD.command         # Lanceur du nœud (double-clic)
├── LANCER_LE_MONITEUR.command      # Lanceur du moniteur (double-clic)
├── setup-mac.sh                     # Script d'installation
├── start-mac.sh                     # Script de démarrage du nœud
├── run-monitor.sh                   # Script de monitoring
├── p2p.key                          # Votre clé d'identité P2P (⚠️ NE PAS PARTAGER)
├── parallax/                        # Code source officiel Parallax
├── venv/                            # Environnement virtuel Python
├── live-monitor.py                  # Moniteur en temps réel
├── mac-monitor.py                   # Moniteur optimisé macOS
└── app.html                         # Interface web de monitoring
```

## 🛠️ Dépannage

### Le nœud ne démarre pas

1. Vérifiez que l'installation est complète :
   ```bash
   ./setup-mac.sh
   ```

2. Vérifiez les logs :
   ```bash
   cat server.log
   ```

3. Réinstallez les dépendances :
   ```bash
   ./fix-dependencies.sh
   ```

### Erreur Python ou dépendances manquantes

```bash
# Réactiver l'environnement virtuel
source venv/bin/activate

# Réinstaller les dépendances
pip install -r parallax/requirements.txt
```

### Le moniteur n'affiche rien

Assurez-vous que le nœud est bien lancé avant de démarrer le moniteur.

### Port 3001 déjà utilisé

Modifiez le port dans `start-mac.sh` :
```bash
# Changez 3001 par un autre port (ex: 3002)
```

## 🔐 Sécurité

### ⚠️ IMPORTANT : Protégez votre clé P2P

Le fichier `p2p.key` contient votre identité unique sur le réseau :
- ❌ **NE JAMAIS** partager ce fichier
- ❌ **NE JAMAIS** le commiter sur GitHub
- ✅ **TOUJOURS** le sauvegarder en lieu sûr
- ✅ **TOUJOURS** le garder privé

### Sauvegarde recommandée

```bash
# Copier votre clé dans un endroit sûr
cp p2p.key ~/Documents/gradient-backup-p2p.key
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🔗 Liens utiles

- [Site officiel Gradient](https://gradient.network)
- [Documentation Parallax](https://docs.gradient.network)
- [Discord Gradient](https://discord.gg/gradient)
- [Twitter Gradient](https://twitter.com/gradientnetwork)

## 📞 Support

Si vous rencontrez des problèmes :
1. Consultez la section [Dépannage](#-dépannage)
2. Ouvrez une [Issue](https://github.com/minculusofia-wq/gradient-optimizer/issues)
3. Rejoignez le [Discord Gradient](https://discord.gg/gradient)

---

**⭐ Si ce projet vous aide, n'hésitez pas à lui donner une étoile !**

*Développé avec ❤️ pour la communauté Gradient*
