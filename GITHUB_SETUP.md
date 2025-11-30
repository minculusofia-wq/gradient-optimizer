# 📤 Guide de publication sur GitHub

Ce guide vous explique comment publier votre projet Gradient Optimizer sur GitHub.

## 🎯 Étape 1 : Créer un dépôt sur GitHub

1. **Connectez-vous à GitHub** : [https://github.com](https://github.com)

2. **Créez un nouveau dépôt** :
   - Cliquez sur le bouton **"+"** en haut à droite
   - Sélectionnez **"New repository"**

3. **Configurez le dépôt** :
   - **Repository name** : `gradient-optimizer` (ou le nom de votre choix)
   - **Description** : `🚀 Simple and optimized Parallax Node runner for macOS - Gradient Network farming tool`
   - **Visibilité** : 
     - ✅ **Public** (recommandé pour partager avec la communauté)
     - ⚠️ **Private** (si vous voulez garder le projet privé)
   - ❌ **NE PAS** cocher "Add a README file" (nous en avons déjà un)
   - ❌ **NE PAS** cocher "Add .gitignore" (nous en avons déjà un)
   - ❌ **NE PAS** cocher "Choose a license" (nous avons déjà MIT)

4. **Cliquez sur "Create repository"**

## 🔗 Étape 2 : Lier votre projet local au dépôt GitHub

Une fois le dépôt créé, GitHub vous affichera des instructions. Utilisez la section **"…or push an existing repository from the command line"**.

### Option A : Avec HTTPS (recommandé pour débuter)

```bash
# Remplacez VOTRE_USERNAME par votre nom d'utilisateur GitHub
git remote add origin https://github.com/VOTRE_USERNAME/gradient-optimizer.git
git branch -M main
git push -u origin main
```

### Option B : Avec SSH (si vous avez configuré une clé SSH)

```bash
# Remplacez VOTRE_USERNAME par votre nom d'utilisateur GitHub
git remote add origin git@github.com:VOTRE_USERNAME/gradient-optimizer.git
git branch -M main
git push -u origin main
```

## 🔐 Étape 3 : Authentification (si nécessaire)

### Si vous utilisez HTTPS :

GitHub vous demandera vos identifiants. Depuis août 2021, vous devez utiliser un **Personal Access Token** au lieu de votre mot de passe.

**Créer un token** :
1. Allez dans **Settings** > **Developer settings** > **Personal access tokens** > **Tokens (classic)**
2. Cliquez sur **"Generate new token"** > **"Generate new token (classic)"**
3. Donnez un nom au token (ex: "Gradient Optimizer")
4. Sélectionnez la portée **"repo"** (accès complet aux dépôts)
5. Cliquez sur **"Generate token"**
6. **Copiez le token** (vous ne pourrez plus le voir après !)
7. Utilisez ce token comme mot de passe lors du push

### Si vous utilisez SSH :

Assurez-vous d'avoir configuré votre clé SSH sur GitHub :
1. Allez dans **Settings** > **SSH and GPG keys**
2. Ajoutez votre clé publique SSH

## ✅ Étape 4 : Vérification

Une fois le push terminé :
1. Actualisez la page de votre dépôt GitHub
2. Vous devriez voir tous vos fichiers
3. Le README.md s'affichera automatiquement sur la page d'accueil

## 🎨 Étape 5 : Personnalisation (optionnel)

### Ajouter des topics

Sur la page de votre dépôt :
1. Cliquez sur l'icône ⚙️ à côté de "About"
2. Ajoutez des topics : `gradient`, `parallax`, `node`, `farming`, `macos`, `cryptocurrency`

### Ajouter une description

Dans la même section "About", ajoutez :
```
🚀 Simple and optimized Parallax Node runner for macOS - Gradient Network farming tool
```

### Ajouter un site web (optionnel)

Si vous avez un site ou une documentation, ajoutez l'URL dans "Website".

## 🔄 Étape 6 : Mises à jour futures

Pour pousser de nouvelles modifications :

```bash
# Ajouter les fichiers modifiés
git add .

# Créer un commit avec un message descriptif
git commit -m "Description de vos modifications"

# Pousser vers GitHub
git push
```

## 📋 Checklist finale

- [ ] Dépôt créé sur GitHub
- [ ] Remote origin configuré
- [ ] Premier push effectué avec succès
- [ ] README.md s'affiche correctement
- [ ] Le fichier `p2p.key` n'apparaît PAS dans le dépôt (vérifié par .gitignore)
- [ ] Topics ajoutés
- [ ] Description configurée

## ⚠️ IMPORTANT : Sécurité

Vérifiez que votre fichier `p2p.key` n'est **JAMAIS** poussé sur GitHub :

```bash
# Vérifier que p2p.key est bien ignoré
git status

# Si p2p.key apparaît dans les fichiers à commiter, ARRÊTEZ !
# Assurez-vous qu'il est dans .gitignore
```

Si vous avez accidentellement poussé `p2p.key` :
1. **Supprimez immédiatement le dépôt GitHub**
2. Générez une nouvelle clé `p2p.key`
3. Recréez le dépôt

## 🎉 Félicitations !

Votre projet est maintenant sur GitHub ! Vous pouvez :
- Partager le lien avec la communauté
- Recevoir des contributions
- Suivre l'historique de vos modifications
- Collaborer avec d'autres développeurs

---

**Besoin d'aide ?** Consultez la [documentation GitHub](https://docs.github.com)
