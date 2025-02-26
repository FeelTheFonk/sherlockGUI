# SherlockGUI

<div align="center">
  <img src="sherlock.png" alt="SherlockGUI Logo" width="200">
  <h3>Interface graphique pour Sherlock</h3>
  <h4>Détecteur de noms d'utilisateur sur les réseaux sociaux</h4>
  
  <p>
    <a href="https://github.com/sherlock-project/sherlock"><img src="https://img.shields.io/badge/Basé%20sur-Sherlock-blue" alt="Based on Sherlock"></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.8%2B-brightgreen" alt="Python 3.8+"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
    <a href="https://github.com/FeelTheFonk/sherlockGui/releases"><img src="https://img.shields.io/github/v/release/FeelTheFonk/sherlockGui" alt="Release"></a>
  </p>
  
  <hr style="width:50%">
</div>

<table>
  <tr>
    <td width="70%">
      <h2>Description</h2>
      <p>SherlockGUI est une interface graphique pour <a href="https://github.com/sherlock-project/sherlock">Sherlock</a>, un outil puissant permettant de rechercher des noms d'utilisateur à travers plus de 400 réseaux sociaux et sites web. Cette interface offre une expérience utilisateur intuitive et rend l'utilisation de Sherlock accessible à tous.</p>
    </td>
    <td width="30%" align="center">
      <img src="docs/images/app-preview.png" alt="Aperçu de l'application" width="100%">
    </td>
  </tr>
</table>

<div style="background-color:#f6f8fa; padding:15px; border-radius:5px; margin:20px 0;">
  <h2>Fonctionnalités</h2>
  <table>
    <tr>
      <td width="50%">
        <ul>
          <li><strong>Interface utilisateur intuitive</strong> avec onglets organisés</li>
          <li><strong>Recherche de plusieurs noms d'utilisateur</strong> en une seule requête</li>
          <li><strong>Support pour plus de 400 plateformes</strong> (réseaux sociaux, forums, sites web)</li>
          <li><strong>Multiples formats d'export</strong> (TXT, CSV, XLSX)</li>
        </ul>
      </td>
      <td width="50%">
        <ul>
          <li><strong>Options avancées</strong> (utilisation de Tor, proxy, timeout personnalisé)</li>
          <li><strong>Sélection/filtrage des sites</strong> pour des recherches ciblées</li>
          <li><strong>Statistiques en temps réel</strong> pendant la recherche</li>
          <li><strong>Interface claire et élégante</strong></li>
        </ul>
      </td>
    </tr>
  </table>
</div>

<hr>

<h2>Installation</h2>

<h3>Prérequis</h3>

<div style="background-color:#f6f8fa; padding:15px; border-radius:5px; margin:10px 0;">
  <ul>
    <li>Python 3.8 ou supérieur</li>
    <li>Sherlock installé sur votre système</li>
  </ul>
</div>

<h3>Méthodes d'installation</h3>

<details>
  <summary><strong>Installation depuis les versions précompilées</strong></summary>
  <div style="padding:15px">
    <ol>
      <li>Téléchargez la dernière version précompilée depuis la <a href="https://github.com/FeelTheFonk/sherlockGui/releases">page des releases</a></li>
      <li>Extrayez l'archive dans le dossier de votre choix</li>
      <li>Exécutez l'application</li>
    </ol>
  </div>
</details>

<details>
  <summary><strong>Installation depuis la source</strong></summary>
  <div style="padding:15px">
    <pre><code>
- Cloner le dépôt
git clone https://github.com/FeelTheFonk/sherlockGui.git
cd sherlock-gui

- Installer les dépendances
pip install -r requirements.txt

- Lancer l'application
python main.py
    </code></pre>
  </div>
</details>

<hr>

<h2>Utilisation</h2>

<div class="usage-guide" style="display:flex; flex-wrap:wrap; justify-content:center; gap:20px; margin:20px 0;">
  <div style="flex:1; min-width:250px; background-color:#f6f8fa; padding:15px; border-radius:5px;">
    <h3>1. Recherche de base</h3>
    <ol>
      <li>Lancez l'application</li>
      <li>Entrez un ou plusieurs noms d'utilisateur (séparés par des espaces)</li>
      <li>Cliquez sur "Lancer la recherche"</li>
      <li>Consultez les résultats dans l'onglet "Résultats"</li>
    </ol>
  </div>
  
  <div style="flex:1; min-width:250px; background-color:#f6f8fa; padding:15px; border-radius:5px;">
    <h3>2. Configuration des options</h3>
    <ol>
      <li>Sélectionnez les formats d'export souhaités (CSV, XLSX)</li>
      <li>Définissez le timeout si nécessaire</li>
      <li>Choisissez entre afficher tous les résultats ou seulement les profils trouvés</li>
      <li>Activez/désactivez les options selon vos besoins</li>
    </ol>
  </div>
  
  <div style="flex:1; min-width:250px; background-color:#f6f8fa; padding:15px; border-radius:5px;">
    <h3>3. Sélection des sites</h3>
    <ol>
      <li>Accédez à l'onglet "Sites Spécifiques"</li>
      <li>Utilisez la recherche pour filtrer les sites</li>
      <li>Sélectionnez les sites individuellement ou utilisez les boutons de sélection rapide</li>
      <li>Retournez à l'onglet "Recherche" pour lancer la recherche</li>
    </ol>
  </div>
</div>

<hr>

<h2>Configuration avancée</h2>

<table>
  <tr>
    <td width="33%" style="vertical-align:top; padding:10px;">
      <h3>Options Tor</h3>
      <p>Pour anonymiser vos recherches via le réseau Tor :</p>
      <ol>
        <li>Assurez-vous que Tor est installé sur votre système</li>
        <li>Activez l'option "Utiliser Tor" dans l'onglet "Options Avancées"</li>
        <li>Optionnellement, activez "Tor unique" pour utiliser un nouveau circuit après chaque requête</li>
      </ol>
    </td>
    <td width="33%" style="vertical-align:top; padding:10px;">
      <h3>Utilisation d'un proxy</h3>
      <p>Pour utiliser un proxy avec SherlockGUI :</p>
      <ol>
        <li>Accédez à l'onglet "Options Avancées"</li>
        <li>Entrez l'URL du proxy (ex: socks5://127.0.0.1:1080)</li>
      </ol>
    </td>
    <td width="33%" style="vertical-align:top; padding:10px;">
      <h3>Fichier JSON personnalisé</h3>
      <p>Pour utiliser votre propre définition de sites :</p>
      <ol>
        <li>Accédez à l'onglet "Options Avancées"</li>
        <li>Spécifiez le chemin vers votre fichier JSON personnalisé</li>
      </ol>
    </td>
  </tr>
</table>

<hr>

<h2>Contribution</h2>

<p>Les contributions sont les bienvenues ! Pour contribuer à SherlockGUI :</p>

<div style="background-color:#f6f8fa; padding:15px; border-radius:5px; margin:10px 0; font-family:monospace;">
  git clone https://github.com/FeelTheFonk/sherlockGui.git<br>
  cd sherlock-gui<br>
  git checkout -b feature/ma-nouvelle-fonctionnalite<br>
  # Développement de votre fonctionnalité<br>
  git commit -m "Ajout de ma nouvelle fonctionnalité"<br>
  git push origin feature/ma-nouvelle-fonctionnalite<br>
  # Créez ensuite une Pull Request sur GitHub
</div>

<p>Veuillez consulter le fichier <a href="CONTRIBUTING.md">CONTRIBUTING.md</a> pour plus de détails sur notre processus de contribution.</p>

<hr>

<h2>Crédits</h2>

<div style="display:flex; flex-wrap:wrap; gap:20px; margin:20px 0;">
  <div style="flex:1; min-width:200px; text-align:center;">
    <img src="https://github.com/sherlock-project/sherlock/blob/master/docs/images/sherlock-logo.png" alt="Sherlock Project" height="60">
    <p>L'outil original sur lequel cette interface est basée</p>
  </div>
  
  <div style="flex:1; min-width:200px; text-align:center;">
    <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python" height="60">
    <p>Le langage de programmation utilisé</p>
  </div>
  
  <div style="flex:1; min-width:200px; text-align:center;">
    <img src="https://raw.githubusercontent.com/MisbahSirnaik/Python-Tkinter/refs/heads/master/icon.ico" alt="Tkinter" height="60">
    <p>La bibliothèque d'interface graphique utilisée</p>
  </div>
</div>