# SherlockGUI

<div align="center">
  <img src="sherlock.png" alt="SherlockGUI Logo" width="200">
  <br>
  <p><strong>Interface graphique pour Sherlock - Détecteur de noms d'utilisateur sur les réseaux sociaux</strong></p>
  <p>
    <a href="https://github.com/sherlock-project/sherlock"><img src="https://img.shields.io/badge/Basé%20sur-Sherlock-blue" alt="Based on Sherlock"></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.8%2B-brightgreen" alt="Python 3.8+"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
    <a href="https://github.com/yourusername/sherlock-gui/releases"><img src="https://img.shields.io/github/v/release/yourusername/sherlock-gui" alt="Release"></a>
  </p>
</div>

## 📋 Description

SherlockGUI est une interface graphique pour [Sherlock](https://github.com/sherlock-project/sherlock), un outil puissant permettant de rechercher des noms d'utilisateur à travers plus de 400 réseaux sociaux et sites web. Cette interface offre une expérience utilisateur intuitive et rend l'utilisation de Sherlock accessible à tous.

## 🌟 Fonctionnalités

- ✅ **Interface utilisateur intuitive** avec onglets organisés
- 🔍 **Recherche de plusieurs noms d'utilisateur** en une seule requête
- 🌐 **Support pour plus de 400 plateformes** (réseaux sociaux, forums, sites web)
- 📊 **Multiples formats d'export** (TXT, CSV, XLSX)
- 🛠️ **Options avancées** (utilisation de Tor, proxy, timeout personnalisé)
- 🔎 **Sélection/filtrage des sites** pour des recherches ciblées
- 📈 **Statistiques en temps réel** pendant la recherche
- 🌙 **Interface claire et élégante**

---

## 💻 Installation

### Prérequis

- Python 3.8 ou supérieur
- Sherlock installé sur votre système

### Méthode 1 : Installation depuis les versions précompilées

1. Téléchargez la dernière version précompilée depuis la [page des releases](https://github.com/yourusername/sherlock-gui/releases)
2. Extrayez l'archive dans le dossier de votre choix
3. Exécutez l'application

### Méthode 2 : Installation depuis la source

```bash
# Cloner le dépôt
git clone https://github.com/FeelTheFonk/sherlockGui.git
cd sherlock-gui

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python main.py
```

---

## 🚀 Utilisation

1. **Lancement de l'application** : Exécutez l'application depuis votre système de fichiers ou via la commande
2. **Saisie des noms d'utilisateur** : Entrez un ou plusieurs noms d'utilisateur (séparés par des espaces)
3. **Configuration des options** : Sélectionnez les options souhaitées (format d'export, timeout, etc.)
4. **Sélection des sites** (optionnel) : Choisissez les sites spécifiques à vérifier
5. **Lancement de la recherche** : Cliquez sur "Lancer la recherche"
6. **Consultation des résultats** : Visualisez les résultats dans l'onglet "Résultats"
7. **Export des résultats** : Exportez les résultats dans le format souhaité

## ⚙️ Configuration avancée

### Options Tor

Si vous souhaitez anonymiser vos recherches, SherlockGUI prend en charge l'utilisation du réseau Tor :

1. Assurez-vous que Tor est installé sur votre système
2. Activez l'option "Utiliser Tor" dans l'onglet "Options Avancées"
3. Optionnellement, activez "Tor unique" pour utiliser un nouveau circuit après chaque requête

### Utilisation d'un proxy

Pour utiliser un proxy avec SherlockGUI :

1. Accédez à l'onglet "Options Avancées"
2. Entrez l'URL du proxy (ex: socks5://127.0.0.1:1080)

### Personnalisation du fichier JSON

Pour utiliser un fichier JSON personnalisé contenant vos propres définitions de sites :

1. Accédez à l'onglet "Options Avancées"
2. Spécifiez le chemin vers votre fichier JSON personnalisé

---

## 👥 Contribution

Les contributions sont les bienvenues ! Pour contribuer à SherlockGUI :

1. Fork le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

Veuillez consulter le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.

---

## 🙏 Crédits

- [Sherlock Project](https://github.com/sherlock-project/sherlock) - L'outil original sur lequel cette interface est basée
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - La bibliothèque d'interface graphique utilisée

---