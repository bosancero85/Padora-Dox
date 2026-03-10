# 🗲 PANDORA - Deep Trace Global Tracker 🗲

![Pandora Header](https://img.shields.io/badge/Version-3.0-magenta?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Termux-blue?style=for-the-badge)

```text
    8888888b.                            888                              
    888   Y88b                           888                              
    888    888                           888                              
    888   d88P 8888b.  88888b.   .d8888b.888  .d8888b.  888d888 8888b.    
    8888888P"     "88b 888 "88b  d88"   8888 d88"   88b 888P"      "88b   
    888       .d888888 888  888  888    8888 888    888 888    .d888888   
    888       888  888 888  888  Y88b  d8888 Y88b  d88P 888    888  188   
    888       "Y888888 888  888  "Y8888P"888  "Y8888P"  888    "Y888888   

          ::: Aplication Development by ✘ Aki_SystemDown® ©2026 :::
                             ::: People ✘ Tracker :::
 
## 📱 Installation in Termux (Android)

Kopiere diese Befehle und füge sie nacheinander in dein Termux-Terminal ein, um **Pandora** zu installieren und zu starten:

```bash
# 1. System-Update & Pakete installieren
pkg update && pkg upgrade -y
pkg install git python -y

# 2. Repository von GitHub klonen
# (Ersetze DEIN_USER durch deinen echten GitHub-Namen)
git clone [https://github.com/bosancero85/Padora-Dox.git](https://github.com/bosancero85/Padora-Dox.git)
cd Padora-Dox

# 3. Falls die Datei ein Leerzeichen hat, korrigieren:
mv "PandoraDox. py" dox.py 2>/dev/null

# 4. Abhängigkeiten installieren
pip install colorama

# 5. Pandora Engine starten
python dox.py

Tipp: Wenn du Pandora das nächste Mal startest, musst du nur noch cd Padora-Dox und python dox.py eingeben.
​🛠 Schnellstart-Shortcut (Optional)
​Möchtest du Pandora mit nur einem Wort starten? Gib dies einmalig in Termux ein:

echo "alias pandora='python ~/Padora-Dox/dox.py'" >> ~/.bashrc && source ~/.bashrc

​⚠️ Disclaimer
​Dieses Tool wurde zu Bildungszwecken im Bereich OSINT entwickelt. Der Entwickler übernimmt keine Verantwortung für die missbräuchliche Verwendung oder den Einsatz gegen Dritte ohne deren Zustimmung.
​Development by ✘ Aki_SystemDown®
