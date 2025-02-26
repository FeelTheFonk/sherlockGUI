import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import subprocess
import threading
import os
import sys
import json
from pathlib import Path
import webbrowser
import time

class SherlockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sherlock GUI")
        self.root.geometry("950x700")
        self.root.minsize(800, 600)
        
        try:
            if sys.platform == "win32":
                self.root.iconbitmap("sherlock.ico")
            else:
                logo = tk.PhotoImage(file="sherlock.png")
                self.root.iconphoto(True, logo)
        except:
            pass
        
        self.usernames_var = tk.StringVar()
        self.folder_output_var = tk.StringVar()
        self.single_output_var = tk.StringVar()
        self.timeout_var = tk.StringVar(value="60")
        self.proxy_var = tk.StringVar()
        self.json_file_var = tk.StringVar()
        self.selected_sites = []
        self.all_sites = []
        
        self.verbose_var = tk.BooleanVar(value=True)
        self.tor_var = tk.BooleanVar(value=False)
        self.unique_tor_var = tk.BooleanVar(value=False)
        self.csv_var = tk.BooleanVar(value=True)
        self.xlsx_var = tk.BooleanVar(value=True)
        self.print_all_var = tk.BooleanVar(value=True)
        self.print_found_var = tk.BooleanVar(value=True)
        self.no_color_var = tk.BooleanVar(value=False)
        self.browse_var = tk.BooleanVar(value=False)
        self.local_var = tk.BooleanVar(value=False)
        self.nsfw_var = tk.BooleanVar(value=True)
        
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))
        self.style.configure("TButton", font=("Helvetica", 10))
        self.style.configure("Header.TLabel", font=("Helvetica", 12, "bold"))
        self.style.configure("Title.TLabel", font=("Helvetica", 16, "bold"))
        self.style.configure("TButton", padding=6)
        
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.background_color = "#f0f0f0"
        self.text_color = "#333333"
        self.success_color = "#27ae60"
        self.warning_color = "#f39c12"
        self.error_color = "#e74c3c"
        
        self.create_widgets()
        
        self.root.configure(bg=self.background_color)
        
        self.center_window()
        
        self.check_sherlock_installed()
        
    def check_sherlock_installed(self):
        try:
            process = subprocess.run(["sherlock", "--version"], 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE, 
                                   text=True, 
                                   timeout=3)
            
            if process.returncode == 0:
                return True
            else:
                messagebox.warning(
                    "Attention", 
                    "Sherlock semble être installé mais rencontre un problème.\nErreur: " + process.stderr)
                return False
                
        except FileNotFoundError:
            messagebox.error(
                "Erreur d'installation", 
                "Sherlock n'est pas installé ou n'est pas dans le PATH du système.\n\n"
                "Installez-le avec la commande:\n"
                "pip install sherlock-project\n\n"
                "Ou depuis le dépôt GitHub:\n"
                "git clone https://github.com/sherlock-project/sherlock.git\n"
                "cd sherlock\n"
                "python -m pip install -r requirements.txt")
            return False
        except Exception as e:
            messagebox.error(
                "Erreur", 
                f"Erreur lors de la vérification de l'installation de sherlock: {str(e)}")
            return False
        
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.main_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.main_tab, text="Recherche")
        
        self.advanced_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.advanced_tab, text="Options Avancées")
        
        self.sites_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.sites_tab, text="Sites Spécifiques")
        
        self.results_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.results_tab, text="Résultats")
        
        self.build_main_tab()
        self.build_advanced_tab()
        self.build_sites_tab()
        self.build_results_tab()
        
    def build_main_tab(self):
        main_frame = ttk.Frame(self.main_tab, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(main_frame, text="Sherlock - Recherche de Profils", style="Title.TLabel")
        title_label.pack(pady=(0, 20))
        
        usernames_frame = ttk.LabelFrame(main_frame, text="Noms d'utilisateur", padding="10")
        usernames_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(usernames_frame, text="Entrez un ou plusieurs noms d'utilisateur (séparés par des espaces):").pack(anchor=tk.W, pady=(0, 5))
        
        username_entry = ttk.Entry(usernames_frame, textvariable=self.usernames_var, width=70)
        username_entry.pack(fill=tk.X, pady=5)
        username_entry.focus()
        
        output_frame = ttk.LabelFrame(main_frame, text="Options de sortie", padding="10")
        output_frame.pack(fill=tk.X, pady=10)
        
        folder_frame = ttk.Frame(output_frame)
        folder_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(folder_frame, text="Dossier de sortie (multiple):").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(folder_frame, textvariable=self.folder_output_var, width=50).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        ttk.Button(folder_frame, text="Parcourir", command=self.browse_folder).pack(side=tk.LEFT, padx=5)
        
        file_frame = ttk.Frame(output_frame)
        file_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(file_frame, text="Fichier de sortie (unique):  ").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(file_frame, textvariable=self.single_output_var, width=50).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        ttk.Button(file_frame, text="Parcourir", command=self.browse_file).pack(side=tk.LEFT, padx=5)
        
        format_frame = ttk.Frame(output_frame)
        format_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(format_frame, text="Formats d'export:").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Checkbutton(format_frame, text="TXT (par défaut)", state="disabled", variable=tk.BooleanVar(value=True)).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(format_frame, text="CSV", variable=self.csv_var).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(format_frame, text="XLSX", variable=self.xlsx_var).pack(side=tk.LEFT, padx=5)
        
        common_options_frame = ttk.LabelFrame(main_frame, text="Options communes", padding="10")
        common_options_frame.pack(fill=tk.X, pady=10)
        
        options_row1 = ttk.Frame(common_options_frame)
        options_row1.pack(fill=tk.X, pady=5)
        
        ttk.Checkbutton(options_row1, text="Verbose/Debug", variable=self.verbose_var).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_row1, text="NSFW", variable=self.nsfw_var).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_row1, text="Afficher tous les résultats", variable=self.print_all_var).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_row1, text="Afficher seulement trouvés", variable=self.print_found_var).pack(side=tk.LEFT, padx=5)
        
        options_row2 = ttk.Frame(common_options_frame)
        options_row2.pack(fill=tk.X, pady=5)
        
        ttk.Checkbutton(options_row2, text="Ouvrir résultats dans navigateur", variable=self.browse_var).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_row2, text="Sans couleur", variable=self.no_color_var).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_row2, text="Utiliser data.json local", variable=self.local_var).pack(side=tk.LEFT, padx=5)
        
        timeout_frame = ttk.Frame(common_options_frame)
        timeout_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(timeout_frame, text="Timeout (secondes):").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(timeout_frame, textvariable=self.timeout_var, width=10).pack(side=tk.LEFT, padx=5)
        
        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill=tk.X, pady=20)
        
        run_button = ttk.Button(action_frame, text="Lancer la recherche", command=self.run_sherlock, width=20)
        run_button.pack(side=tk.RIGHT, padx=5)
        
        clear_button = ttk.Button(action_frame, text="Réinitialiser", command=self.reset_form, width=15)
        clear_button.pack(side=tk.RIGHT, padx=5)
        
    def build_advanced_tab(self):
        advanced_frame = ttk.Frame(self.advanced_tab, padding="10")
        advanced_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(advanced_frame, text="Options Avancées", style="Title.TLabel")
        title_label.pack(pady=(0, 20))
        
        tor_frame = ttk.LabelFrame(advanced_frame, text="Options Tor", padding="10")
        tor_frame.pack(fill=tk.X, pady=10)
        
        ttk.Checkbutton(tor_frame, text="Utiliser Tor (augmente le temps d'exécution)", 
                        variable=self.tor_var).pack(anchor=tk.W, pady=5)
        ttk.Checkbutton(tor_frame, text="Tor unique (nouveau circuit après chaque requête)", 
                        variable=self.unique_tor_var).pack(anchor=tk.W, pady=5)
        
        proxy_frame = ttk.LabelFrame(advanced_frame, text="Paramètres du Proxy", padding="10")
        proxy_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(proxy_frame, text="URL du Proxy (ex: socks5://127.0.0.1:1080):").pack(anchor=tk.W, pady=(0, 5))
        ttk.Entry(proxy_frame, textvariable=self.proxy_var, width=50).pack(fill=tk.X, pady=5)
        
        json_frame = ttk.LabelFrame(advanced_frame, text="Fichier JSON personnalisé", padding="10")
        json_frame.pack(fill=tk.X, pady=10)
        
        json_entry_frame = ttk.Frame(json_frame)
        json_entry_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(json_entry_frame, text="Fichier JSON:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(json_entry_frame, textvariable=self.json_file_var, width=50).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        ttk.Button(json_entry_frame, text="Parcourir", command=self.browse_json).pack(side=tk.LEFT, padx=5)
        
        info_frame = ttk.LabelFrame(advanced_frame, text="Notes", padding="10")
        info_frame.pack(fill=tk.X, pady=10)
        
        info_text = ("• L'utilisation de Tor nécessite que Tor soit installé et dans le PATH système\n"
                    "• Si vous spécifiez à la fois un proxy et Tor, seul le proxy sera utilisé\n"
                    "• Le fichier JSON peut être local ou une URL valide\n"
                    "• Toutes les options sont configurées par défaut pour une recherche exhaustive")
        
        info_label = ttk.Label(info_frame, text=info_text, justify=tk.LEFT)
        info_label.pack(anchor=tk.W, pady=5)
        
    def build_sites_tab(self):
        sites_frame = ttk.Frame(self.sites_tab, padding="10")
        sites_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(sites_frame, text="Sélection de Sites Spécifiques", style="Title.TLabel")
        title_label.pack(pady=(0, 20))
        
        desc_label = ttk.Label(sites_frame, text="Sélectionnez les sites spécifiques pour limiter la recherche.\nSi aucun site n'est sélectionné, tous les sites disponibles seront vérifiés.")
        desc_label.pack(anchor=tk.W, pady=(0, 10))
        
        search_frame = ttk.Frame(sites_frame)
        search_frame.pack(fill=tk.X, pady=5)
        
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_sites)
        
        ttk.Label(search_frame, text="Rechercher:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(search_frame, textvariable=self.search_var, width=30).pack(side=tk.LEFT, padx=5)
        
        select_frame = ttk.Frame(sites_frame)
        select_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(select_frame, text="Tout sélectionner", command=self.select_all_sites).pack(side=tk.LEFT, padx=5)
        ttk.Button(select_frame, text="Tout désélectionner", command=self.deselect_all_sites).pack(side=tk.LEFT, padx=5)
        ttk.Button(select_frame, text="Inverser la sélection", command=self.invert_selection).pack(side=tk.LEFT, padx=5)
        
        sites_list_frame = ttk.Frame(sites_frame)
        sites_list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        scrollbar = ttk.Scrollbar(sites_list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.sites_tree = ttk.Treeview(sites_list_frame, yscrollcommand=scrollbar.set, selectmode="extended")
        self.sites_tree.pack(fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.sites_tree.yview)
        
        self.sites_tree["columns"] = ("selected")
        self.sites_tree.column("#0", width=250, minwidth=250)
        self.sites_tree.column("selected", width=100, minwidth=100, anchor=tk.CENTER)
        
        self.sites_tree.heading("#0", text="Site", anchor=tk.W)
        self.sites_tree.heading("selected", text="Sélectionné", anchor=tk.CENTER)
        
        self.populate_sites_list()
        
        self.sites_tree.bind("<Double-1>", self.toggle_site_selection)
        
    def build_results_tab(self):
        results_frame = ttk.Frame(self.results_tab, padding="10")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(results_frame, text="Résultats de la Recherche", style="Title.TLabel")
        title_label.pack(pady=(0, 10))
        
        toolbar_frame = ttk.Frame(results_frame)
        toolbar_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(toolbar_frame, text="Effacer les résultats", command=self.clear_results).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar_frame, text="Exporter les résultats", command=self.export_results).pack(side=tk.LEFT, padx=5)
        
        self.progress_frame = ttk.Frame(results_frame)
        self.progress_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(self.progress_frame, text="Progression:").pack(side=tk.LEFT, padx=(0, 5))
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient=tk.HORIZONTAL, length=100, mode='indeterminate', variable=self.progress_var)
        self.progress_bar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.results_text = scrolledtext.ScrolledText(results_frame, width=80, height=20, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True, pady=10)
        self.results_text.config(state=tk.DISABLED)
        
        stats_frame = ttk.LabelFrame(results_frame, text="Statistiques", padding="10")
        stats_frame.pack(fill=tk.X, pady=5)
        
        stats_inner_frame = ttk.Frame(stats_frame)
        stats_inner_frame.pack(fill=tk.X)
        
        ttk.Label(stats_inner_frame, text="Total des sites vérifiés:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Label(stats_inner_frame, text="Profils trouvés:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Label(stats_inner_frame, text="Temps d'exécution:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        
        self.total_sites_var = tk.StringVar(value="0")
        self.found_profiles_var = tk.StringVar(value="0")
        self.execution_time_var = tk.StringVar(value="0s")
        
        ttk.Label(stats_inner_frame, textvariable=self.total_sites_var).grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
        ttk.Label(stats_inner_frame, textvariable=self.found_profiles_var).grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        ttk.Label(stats_inner_frame, textvariable=self.execution_time_var).grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exécuter la recherche", command=self.run_sherlock)
        file_menu.add_command(label="Exporter les résultats", command=self.export_results)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.root.quit)
        menubar.add_cascade(label="Fichier", menu=file_menu)
        
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Réinitialiser le formulaire", command=self.reset_form)
        edit_menu.add_command(label="Effacer les résultats", command=self.clear_results)
        menubar.add_cascade(label="Edition", menu=edit_menu)
        
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="À propos", command=self.show_about)
        help_menu.add_command(label="Aide en ligne", 
                             command=lambda: webbrowser.open("https://github.com/sherlock-project/sherlock"))
        menubar.add_cascade(label="Aide", menu=help_menu)
        
        self.root.config(menu=menubar)

    def show_about(self):
        messagebox.showinfo(
            "À propos", 
            "Sherlock GUI - Interface graphique pour Sherlock\n\n"
            "Sherlock est un outil pour rechercher des noms d'utilisateur "
            "sur différents réseaux sociaux et sites web.\n\n"
            "Projet Sherlock: https://github.com/sherlock-project/sherlock")
        
    def get_all_supported_sites(self):
        sites = [
            "1337x", "2Dimensions", "7Cups", "9GAG", "APClips", "About.me", "Academia.edu", 
            "AdmireMe.Vip", "Airbit", "Airliners", "All Things Worn", "AllMyLinks", "AniWorld", 
            "Anilist", "Apple Developer", "Apple Discussions", "Archive of Our Own", "Archive.org", 
            "ArtStation", "Asciinema", "Ask Fedora", "Atcoder", "Audiojungle", "Autofrage", "Avizo", 
            "BOOTH", "Bandcamp", "Bazar.cz", "Behance", "Bezuzyteczna", "BiggerPockets", "BioHacking", 
            "BitBucket", "Bitwarden Forum", "Blipfoto", "Blogger", "Bluesky", "BoardGameGeek", 
            "BongaCams", "Bookcrossing", "BraveCommunity", "BugCrowd", "BuyMeACoffee", "BuzzFeed", 
            "CGTrader", "CNET", "CSSBattle", "CTAN", "Caddy Community", "Car Talk Community", 
            "Carbonmade", "Career.habr", "Championat", "Chaos", "Chatujme.cz", "ChaturBate", "Chess", 
            "Choice Community", "Clapper", "CloudflareCommunity", "Clozemaster", "Clubhouse", 
            "Code Snippet Wiki", "Codeberg", "Codecademy", "Codechef", "Codeforces", "Codepen", 
            "Coders Rank", "Coderwall", "Codewars", "Coinvote", "ColourLovers", "Contently", 
            "Coroflot", "Cracked", "Crevado", "Crowdin", "Cryptomator Forum", "Cults3D", 
            "CyberDefenders", "DEV Community", "DMOJ", "DailyMotion", "Dealabs", "DeviantART", 
            "DigitalSpy", "Discogs", "Discord", "Discuss.Elastic.co", "Disqus", "Docker Hub", 
            "Dribbble", "Duolingo", "Eintracht Frankfurt Forum", "Empretienda AR", "Envato Forum", 
            "Erome", "Exposure", "EyeEm", "F3.cool", "Fameswap", "Fandom", "Fanpop", "Finanzfrage", 
            "Flickr", "Flightradar24", "Flipboard", "Football", "FortniteTracker", "Forum Ophilia", 
            "Fosstodon", "Freelance.habr", "Freelancer", "Freesound", "GNOME VCS", "GaiaOnline", 
            "Gamespot", "GeeksforGeeks", "Genius (Artists)", "Genius (Users)", "Gesundheitsfrage", 
            "GetMyUni", "Giant Bomb", "Giphy", "GitBook", "GitHub", "GitLab", "Gitea", "Gitee", 
            "GoodReads", "Google Play", "Gradle", "Grailed", "Gravatar", "Gumroad", "Gutefrage", 
            "HackTheBox", "Hackaday", "HackenProof (Hackers)", "HackerEarth", "HackerNews", "HackerOne", 
            "HackerRank", "Harvard Scholar", "Hashnode", "Heavy-R", "Holopin", "Houzz", "HubPages", 
            "Hubski", "HudsonRock", "Hugging Face", "IFTTT", "IRC-Galleria", "Icons8 Community", 
            "Image Fap", "ImgUp.cz", "Imgur", "Instagram", "Instructables", "Intigriti", "Ionic Forum", 
            "Issuu", "Itch.io", "Itemfix", "Jellyfin Weblate", "Jimdo", "Joplin Forum", "Kaggle", 
            "Keybase", "Kick", "Kik", "Kongregate", "LOR", "Launchpad", "LeetCode", "LessWrong", 
            "Letterboxd", "LibraryThing", "Lichess", "LinkedIn", "Linktree", "Listed", "LiveJournal", 
            "Lobsters", "LottieFiles", "LushStories", "MMORPG Forum", "Medium", "Memrise", "Minecraft", 
            "MixCloud", "Monkeytype", "Motherless", "Motorradfrage", "MyAnimeList", "MyMiniFactory", 
            "Mydramalist", "Myspace", "NICommunityForum", "NationStates Nation", "NationStates Region", 
            "Naver", "Needrom", "Newgrounds", "Nextcloud Forum", "Nightbot", "Ninja Kiwi", 
            "NintendoLife", "NitroType", "NotABug.org", "Nyaa.si", "OpenStreetMap", "Opensource", 
            "OurDJTalk", "PCGamer", "PSNProfiles.com", "Packagist", "Pastebin", "Patreon", 
            "PentesterLab", "PepperIT", "Periscope", "Pinkbike", "PlayStore", "PocketStars", 
            "Pokemon Showdown", "Polarsteps", "Polygon", "Polymart", "Pornhub", "ProductHunt", 
            "PromoDJ", "PyPi", "Rajce.net", "Rarible", "Rate Your Music", "Rclone Forum", "RedTube", 
            "Redbubble", "Reddit", "Reisefrage", "Replit.com", "ResearchGate", "ReverbNation", 
            "Roblox", "RocketTube", "RoyalCams", "RubyGems", "Rumble", "RuneScape", "SWAPD", 
            "Sbazar.cz", "Scratch", "Scribd", "ShitpostBot5000", "Signal", "Sketchfab", "Slack", 
            "Slant", "Slashdot", "SlideShare", "Slides", "SmugMug", "Smule", "Snapchat", "SoundCloud", 
            "SourceForge", "SoylentNews", "Speedrun.com", "Spells8", "Splice", "Splits.io", "Sporcle", 
            "Sportlerfrage", "SportsRU", "Spotify", "Star Citizen", "Steam Community (Group)", 
            "Steam Community (User)", "Strava", "SublimeForum", "TETR.IO", "TRAKTRAIN", "Telegram", 
            "Tellonym.me", "Tenor", "ThemeForest", "Tiendanube", "TnAFlix", "Topcoder", "TorrentGalaxy", 
            "TradingView", "Trakt", "TrashboxRU", "Trawelling", "Trello", "TryHackMe", "Tuna", 
            "Tweakers", "Twitter", "Typeracer", "Ultimate-Guitar", "Unsplash", "Untappd", "VK", "VLR", 
            "VSCO", "Velog", "Velomania", "Venmo", "Vero", "Vimeo", "VirusTotal", "WICG Forum", 
            "Warrior Forum", "Wattpad", "WebNode", "Weblate", "Weebly", "Wikidot", "Wikipedia", 
            "Windy", "Wix", "WolframalphaForum", "WordPress", "WordPressOrg", "Wordnik", "Wykop", 
            "Xbox Gamertag", "Xvideos", "YandexMusic", "YouNow", "YouPic", "YouPorn", "YouTube", 
            "akniga", "authorSTREAM", "babyblogRU", "chaos.social", "couchsurfing", "d3RU", "dailykos", 
            "datingRU", "devRant", "drive2", "eGPU", "eintracht", "exophase", "fixya", "fl", 
            "forum_guns", "freecodecamp", "furaffinity", "geocaching", "habr", "hackster", "hunting", 
            "igromania", "interpals", "irecommend", "jbzd.com.pl", "jeuxvideo", "kaskus", "kofi", 
            "kwork", "last.fm", "leasehackr", "livelib", "mastodon.cloud", "mastodon.social", 
            "mastodon.xyz", "mercadolivre", "minds", "moikrug", "mstdn.io", "nairaland.com", "nnRU", 
            "note", "npm", "omg.lol", "opennet", "osu!", "phpRU", "pikabu", "pr0gramm", "prog.hu", 
            "satsisRU", "sessionize", "social.tchncs.de", "spletnik", "svidbook", "threads", 
            "toster", "uid", "xHamster", "znanylekarz.pl"
        ]
        return sorted(sites)

    def populate_sites_list(self):
        try:
            sherlock_path = self.find_sherlock_data_path()
            if sherlock_path:
                with open(sherlock_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                sites = list(data.keys())
            else:
                sites = self.get_all_supported_sites()
        except Exception as e:
            sites = self.get_all_supported_sites()
        
        for item in self.sites_tree.get_children():
            self.sites_tree.delete(item)
        
        for site in sites:
            self.sites_tree.insert("", "end", text=site, values=("Non"))
            
        self.all_sites = sites
    
    def find_sherlock_data_path(self):
        possible_paths = [
            "sherlock/data.json",
            os.path.expanduser("~/.local/lib/python3.*/site-packages/sherlock/data.json"),
            "./data.json"
        ]
        
        for path in possible_paths:
            if '*' in path:
                import glob
                matches = glob.glob(path)
                if matches:
                    return matches[0]
            elif os.path.exists(path):
                return path
        
        return None

    def filter_sites(self, *args):
        search_term = self.search_var.get().lower()
        
        for item in self.sites_tree.get_children():
            self.sites_tree.delete(item)
        
        for site in self.all_sites:
            if search_term in site.lower():
                is_selected = "Oui" if site in self.selected_sites else "Non"
                self.sites_tree.insert("", "end", text=site, values=(is_selected))
    
    def select_all_sites(self):
        for item in self.sites_tree.get_children():
            site = self.sites_tree.item(item, "text")
            if site not in self.selected_sites:
                self.selected_sites.append(site)
            self.sites_tree.item(item, values=("Oui"))
    
    def deselect_all_sites(self):
        self.selected_sites = []
        for item in self.sites_tree.get_children():
            self.sites_tree.item(item, values=("Non"))
    
    def invert_selection(self):
        for item in self.sites_tree.get_children():
            site = self.sites_tree.item(item, "text")
            current_state = self.sites_tree.item(item, "values")[0]
            
            if current_state == "Oui":
                self.sites_tree.item(item, values=("Non"))
                if site in self.selected_sites:
                    self.selected_sites.remove(site)
            else:
                self.sites_tree.item(item, values=("Oui"))
                if site not in self.selected_sites:
                    self.selected_sites.append(site)
    
    def toggle_site_selection(self, event):
        item = self.sites_tree.identify('item', event.x, event.y)
        if item:
            site = self.sites_tree.item(item, "text")
            current_state = self.sites_tree.item(item, "values")[0]
            
            if current_state == "Oui":
                self.sites_tree.item(item, values=("Non"))
                if site in self.selected_sites:
                    self.selected_sites.remove(site)
            else:
                self.sites_tree.item(item, values=("Oui"))
                if site not in self.selected_sites:
                    self.selected_sites.append(site)
    
    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_output_var.set(folder)
    
    def browse_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file:
            self.single_output_var.set(file)
    
    def browse_json(self):
        file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if file:
            self.json_file_var.set(file)
    
    def reset_form(self):
        self.usernames_var.set("")
        self.folder_output_var.set("")
        self.single_output_var.set("")
        self.timeout_var.set("60")
        self.proxy_var.set("")
        self.json_file_var.set("")
        
        self.verbose_var.set(True)
        self.tor_var.set(False)
        self.unique_tor_var.set(False)
        self.csv_var.set(True)
        self.xlsx_var.set(True)
        self.print_all_var.set(True)
        self.print_found_var.set(True)
        self.no_color_var.set(False)
        self.browse_var.set(True)
        self.local_var.set(False)
        self.nsfw_var.set(True)
        
        self.selected_sites = []
        self.deselect_all_sites()
        
        self.clear_results()
    
    def clear_results(self):
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)
        
        self.total_sites_var.set("0")
        self.found_profiles_var.set("0")
        self.execution_time_var.set("0s")
    
    def export_results(self):
        if not self.results_text.get(1.0, tk.END).strip():
            messagebox.showinfo("Information", "Aucun résultat à exporter.")
            return
        
        file = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(self.results_text.get(1.0, tk.END))
            messagebox.showinfo("Exportation réussie", f"Les résultats ont été exportés vers {file}")
    
    def run_sherlock(self):
        usernames = self.usernames_var.get().strip()
        if not usernames:
            messagebox.showerror("Erreur", "Veuillez entrer au moins un nom d'utilisateur.")
            return
        
        cmd = ["sherlock"]
        
        if self.verbose_var.get():
            cmd.append("--verbose")
        
        has_multiple_usernames = " " in usernames
        
        if has_multiple_usernames:
            if self.folder_output_var.get():
                cmd.extend(["--folderoutput", self.folder_output_var.get()])
        else:
            if self.single_output_var.get():
                cmd.extend(["--output", self.single_output_var.get()])
            elif self.folder_output_var.get():
                cmd.extend(["--folderoutput", self.folder_output_var.get()])
        
        if self.tor_var.get():
            cmd.append("--tor")
        
        if self.unique_tor_var.get():
            cmd.append("--unique-tor")
        
        if self.csv_var.get():
            cmd.append("--csv")
        
        if self.xlsx_var.get():
            cmd.append("--xlsx")
        
        for site in self.selected_sites:
            cmd.extend(["--site", site])
        
        if self.proxy_var.get():
            cmd.extend(["--proxy", self.proxy_var.get()])
        
        if self.json_file_var.get():
            cmd.extend(["--json", self.json_file_var.get()])
        
        if self.timeout_var.get():
            cmd.extend(["--timeout", self.timeout_var.get()])
        
        if self.print_all_var.get():
            cmd.append("--print-all")
        
        if self.print_found_var.get():
            cmd.append("--print-found")
        
        if self.no_color_var.get():
            cmd.append("--no-color")
        
        if self.browse_var.get():
            cmd.append("--browse")
        
        if self.local_var.get():
            cmd.append("--local")
        
        if self.nsfw_var.get():
            cmd.append("--nsfw")
        
        cmd.extend(usernames.split())
        
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "Exécution de la commande:\n")
        self.results_text.insert(tk.END, " ".join(cmd) + "\n\n")
        self.results_text.insert(tk.END, "Recherche en cours...\n")
        self.results_text.config(state=tk.DISABLED)
        
        self.notebook.select(self.results_tab)
        
        self.progress_bar.start()
        
        self.sherlock_thread = threading.Thread(target=self.execute_sherlock, args=(cmd,))
        self.sherlock_thread.daemon = True
        self.sherlock_thread.start()
    
    def execute_sherlock(self, cmd):
        start_time = time.time()
        
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                bufsize=1
            )
            
            sites_checked = 0
            profiles_found = 0
            
            for line in process.stdout:
                self.update_results(line)
                
                if "[+]" in line:
                    profiles_found += 1
                
                if "Checking " in line:
                    sites_checked += 1
                
                self.total_sites_var.set(str(sites_checked))
                self.found_profiles_var.set(str(profiles_found))
                
                elapsed_time = time.time() - start_time
                self.execution_time_var.set(f"{elapsed_time:.2f}s")
            
            stderr_output, _ = process.communicate()
            if stderr_output:
                self.update_results("\nErreurs:\n" + stderr_output)
            
            process.wait()
            
            elapsed_time = time.time() - start_time
            self.update_results(f"\nRecherche terminée en {elapsed_time:.2f} secondes.")
            self.update_results(f"Profils trouvés: {profiles_found}")
            self.update_results(f"Sites vérifiés: {sites_checked}")
            
            self.execution_time_var.set(f"{elapsed_time:.2f}s")
            
        except Exception as e:
            self.update_results(f"\nErreur lors de l'exécution: {str(e)}")
        
        finally:
            self.root.after(0, self.progress_bar.stop)
    
    def update_results(self, text):
        def update():
            self.results_text.config(state=tk.NORMAL)
            self.results_text.insert(tk.END, text)
            self.results_text.see(tk.END)
            self.results_text.config(state=tk.DISABLED)
        
        self.root.after(0, update)

if __name__ == "__main__":
    root = tk.Tk()
    app = SherlockGUI(root)
    app.create_menu()
    root.mainloop()