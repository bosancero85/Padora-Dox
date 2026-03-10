import os
import sys
import time
import random
import webbrowser
from datetime import datetime
from colorama import init, Fore, Style

# Initialisierung für Farben
init(autoreset=True)

# Ordner für Logs erstellen
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def matrix_rain(duration=5):
    os.system('cls' if os.name == 'nt' else 'clear')
    symbols = ["0", "1", " ", "!", "#", "$", "%", "&", "*", "+", "X", "Y", "Z", "ｦ", "ｱ", "ｳ", "ｴ"]
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    width = 100 
    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            line = "".join(random.choice(symbols) for _ in range(width))
            color = random.choice(colors)
            print(color + Style.BRIGHT + line)
            time.sleep(0.06)
    except KeyboardInterrupt:
        pass
    print(Style.RESET_ALL)

def print_rainbow_branding():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = r"""
    8888888b.                            888                              
    888   Y88b                           888                              
    888    888                           888                              
    888   d88P 8888b.  88888b.   .d8888b.888  .d8888b.  888d888 8888b.    
    8888888P"     "88b 888 "88b  d88"   8888 d88"   88b 888P"      "88b   
    888       .d888888 888  888  888    8888 888    888 888    .d888888   
    888       888  888 888  888  Y88b  d8888 Y88b  d88P 888    888  888   
    888       "Y888888 888  888  "Y8888P"888  "Y8888P"  888    "Y888888   

          ::: Aplication Development by ✘ 𝘼𝙠𝙞_SystemDown® ©2026 :::
                             ::: Peolpe ✘ Tracker :::
    """
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    lines = logo.split('\n')
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        print(color + Style.BRIGHT + line + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "-"*75 + "\n")

def rainbow_loading_bar(length=40):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    print(f"{Fore.WHITE}Durchsuche globale Datenbanken nach Registrierungen...")
    for i in range(length + 1):
        color = colors[i % len(colors)]
        percent = int((i / length) * 100)
        bar = "█" * i + "-" * (length - i)
        sys.stdout.write(f"\r{color}[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.04)
    print(f"\n{Fore.GREEN}Pandora Engine bereit.\n")

def log_results(category, target, urls):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{LOG_DIR}/scan_{category}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"PANDORA FULL SCAN REPORT\nTarget: {target}\nCategory: {category}\n\n")
        for url in urls:
            f.write(f"- {url}\n")
    return filename

def global_search(choice, query):
    if not query: return
    urls = []
    clean_q = query.replace(' ', '')

    # KATEGORIE 1: NAME / USERNAME / SOCIAL / DATING / STREAMING
    if choice in ["1", "00"]:
        urls += [
            f"https://www.google.com/search?q=\"{query}\"",
            f"https://www.instagram.com/{clean_q}/",
            f"https://twitter.com/{clean_q}",
            f"https://www.facebook.com/search/top/?q={query}",
            f"https://www.tiktok.com/@{clean_q}",
            f"https://www.twitch.tv/{clean_q}",
            f"https://kick.com/{clean_q}",
            f"https://www.snapchat.com/add/{clean_q}",
            f"https://www.pinterest.com/{clean_q}",
            f"https://www.reddit.com/user/{query}",
            f"https://www.linkedin.com/search/results/all/?keywords={query}",
            f"https://www.google.com/search?q=site:tinder.com+\"{query}\"",
            f"https://www.google.com/search?q=site:lovoo.com+\"{query}\"",
            f"https://www.google.com/search?q=site:badoo.com+\"{query}\"",
            f"https://www.google.com/search?q=site:onlyfans.com+\"{query}\"",
            f"https://steamcommunity.com/id/{clean_q}"
        ]

    # KATEGORIE 2: PHONE
    if choice in ["2", "00"]:
        urls += [
            f"https://www.tellows.de/num/{query}",
            f"https://www.sync.me/search?number={query}",
            f"https://www.truecaller.com/search/de/{query}",
            f"https://www.google.com/search?q=\"{query}\""
        ]

    # KATEGORIE 3: DISCORD
    if choice in ["3", "00"]:
        urls += [
            f"https://discord.id/?id={query}",
            f"https://discordlookup.com/user/{query}",
            f"https://lookup.guru/id/{query}"
        ]

    # KATEGORIE 4: EMAIL
    if choice in ["4", "00"]:
        urls += [
            f"https://haveibeenpwned.com/account/{query}",
            f"https://intelx.io/?s={query}",
            f"https://email-checker.net/check?email={query}",
            f"https://www.google.com/search?q=\"{query}\""
        ]

    # KATEGORIE 5: IP
    if choice in ["5", "00"]:
        urls += [
            f"https://ipinfo.io/{query}",
            f"https://www.shodan.io/host/{query}",
            f"https://iknowwhatyoudownload.com/en/peer/?ip={query}",
            f"https://www.abuseipdb.com/check/{query}"
        ]

    print(f"\n{Fore.YELLOW}[!] Starte Deep-Scan für: {Fore.WHITE}{query}")
    for url in urls:
        print(f"{Fore.CYAN}[>] Abfrage: {Fore.WHITE}{url}")
        webbrowser.open(url)
        time.sleep(0.4)
    
    log_file = log_results(choice, query, urls)
    print(f"\n{Fore.GREEN}[+] Scan abgeschlossen. Log: {Fore.WHITE}{log_file}")

def main():
    try:
        matrix_rain(5)
        while True:
            print_rainbow_branding()
            rainbow_loading_bar()
            
            print(f"{Fore.WHITE}Wähle Kategorie:")
            print(f"{Fore.MAGENTA}00. ALL (Deep Scan alles)")
            print(f"{Fore.CYAN}1. Name / Username")
            print(f"{Fore.CYAN}2. Phone")
            print(f"{Fore.CYAN}3. Discord ID")
            print(f"{Fore.CYAN}4. E-Mail")
            print(f"{Fore.CYAN}5. IP")
            print(f"{Fore.RED}0. End")
            print(f"{Fore.YELLOW}b. Back")
            
            choice = input(f"\n{Fore.MAGENTA}Pandora > {Fore.WHITE}").lower()
            
            if choice == '0': break
            elif choice == 'b': continue
            
            cat_map = {"00": "FULL TARGET", "1": "Name", "2": "Phone", "3": "Discord", "4": "Email", "5": "IP"}
            
            if choice in cat_map:
                target = input(f"{Fore.GREEN}Gib {cat_map[choice]} ein: {Fore.WHITE}")
                global_search(choice, target)
                input(f"\n{Fore.YELLOW}Scan beendet. Drücke Enter...")
            else:
                time.sleep(1)

    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
