import os
import re
from datetime import datetime
import fade
import subprocess

# -> Crafted by the finest ChatGptnesium you can find, a very rare ore <- #
# -> Credits: chat.openai.com and github.com/Firoxus @ firox.xyz :3333 <- # 

subprocess.run('cls', shell=True)

tex2t = """
/$$$$$$$$ /$$                    
| $$_____/| $$                    
| $$      | $$ /$$   /$$ /$$   /$$
| $$$$$   | $$| $$  | $$|  $$ /$$/
| $$__/   | $$| $$  | $$ \  $$$$/ 
| $$      | $$| $$  | $$  >$$  $$ 
| $$      | $$|  $$$$$$/ /$$/\  $$
|__/      |__/ \______/ |__/  \__/ 
"""
faded_text = fade.greenblue(tex2t)

print(faded_text)

def create_directory_if_not_exists(path):
    """Create the directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def find_password_files(logs_dir):
    """Find and return paths to all 'passwords.txt' or 'Passwords.txt' files in the logs_dir directory."""
    password_files = []
    for root, dirs, files in os.walk(logs_dir):
        for file in files:
            if file.lower() == 'passwords.txt':
                password_files.append(os.path.join(root, file))
    return password_files

def extract_login_info(file_path):
    """Extract usernames and passwords from 'passwords.txt' files for various services."""
    login_info = {
        'Valorant': [],
        'Disney+': [],
        'HBO Max': [],
        'Netflix': [],
        'Steam': [],
        'Fortnite': [],
        'McDonalds': [],
        'Discord': [],
        'Xbox Live': [],
        'Pinterest': [],
        'Twitch': [],
        'Instagram': [],
        'LibreCraft': [],
        'Zoom': [],
        'Roblox': [],
        'MediaFire': [],
        'DeviantArt': [],
        'Aternos': [],
        'KFC': [],
        'BurgerKing': [],
        'EpicGames_Xbox': [],
        'Amazon': [],
        'EpicGames': [],
        'EpicGames_PSN': [],
        'Spotify': [],
        'UnknownCheats': [],
        'Activision': [],
        'FirstMail': [],
        'Kick': [],
        'AppleID': [],
        'BattleNet': [],
        'Restorecord': [],
        'NordVPN': [],
        'PayPal': [],
        'LeagueOfLegends': [],
        'Crunchyroll': [],  
        'Snapchat': [],
    }

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

     
        patterns = {
            'Valorant': r'https://auth\.riotgames\.com/login[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)',
            'Disney+': r'https://www\.disneyplus\.com/[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)',
            'HBO Max': r'https://play\.hbomax\.com/[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)',
            'Netflix': r'https://www\.netflix\.com/[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)',
            'Steam': r'https://steamcommunity\.com[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Fortnite': r'https://www\.fortnite\.com/id/login/epic[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'McDonalds': r'(?i)mcdonalds[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)',
            'Discord': r'(?i)discord[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Xbox Live': r'(?i)login\.live\.com[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Pinterest': r'(?i)pinterest[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Twitch': r'(?i)twitch[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Instagram': r'(?i)instagram[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'LibreCraft': r'(?i)librecraft\.com[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Zoom': r'(?i)zoom[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Roblox': r'(?i)roblox[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'MediaFire': r'(?i)mediafire[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'DeviantArt': r'(?i)deviantart[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Aternos': r'(?i)aternos\.org[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'KFC': r'(?i)kfc[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'BurgerKing': r'(?i)burgerking[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'EpicGames_Xbox': r'(?i)epicgames\.com/id/link/xbl[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Amazon': r'(?i)amazon[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'EpicGames': r'(?i)epicgames\.com/id/login[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'EpicGames_PSN': r'(?i)epicgames\.com/id/login/psn[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Spotify': r'(?i)spotify[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'UnknownCheats': r'(?i)unknowncheats\.me[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Activision': r'(?i)activision[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'FirstMail': r'(?i)firstmail[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Kick': r'(?i)kick\.com[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'AppleID': r'(?i)appleid\.apple\.com[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'BattleNet': r'(?i)account\.battle\.net[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Restorecord': r'(?i)restorecord\.com[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'NordVPN': r'(?i)nordvpn[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'PayPal': r'(?i)paypal[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'LeagueOfLegends': r'(?i)leagueoflegends\.com[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Crunchyroll': r'(?i)crunchyroll[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
            'Snapchat': r'(?i)snapchat[\s\S]*?Username:\s*(\S+)[\s\S]*?Password:\s*(\S+)', 
        }

        for service, pattern in patterns.items():
            matches = re.findall(pattern, content)
            for match in matches:
                username, password = match
                login_info[service].append((username, password))
    
    return login_info

def save_login_info(results_dir, login_info):
    """Save extracted usernames and passwords to respective text files."""
    create_directory_if_not_exists(results_dir)

    for service, info in login_info.items():
        if info:
            file_path = os.path.join(results_dir, f'{service}.txt')
            with open(file_path, 'w', encoding='utf-8') as file:
                for username, password in info:
                    file.write(f'{username}\n{password}\n\n')

        eindreidreisieben = f"""{get_current_datetime()} Saved {service}"""
        faded_text1337 = fade.greenblue(eindreidreisieben)
        print(faded_text1337)

def get_current_datetime():
    return datetime.now().strftime('[ %Y-%m-%d - %H:%M:%S ]')


def main():
    build_dir = os.getcwd()
    logs_dir = os.path.join(build_dir, 'logs')
    results_dir = os.path.join(build_dir, 'results')



    password_files = find_password_files(logs_dir)
    
    if not password_files:
        print(f'{get_current_datetime()} No passwords.txt files found in the logs directory.')
        return
    

    all_login_info = {
        'Valorant': [],
        'Disney+': [],
        'HBO Max': [],
        'Netflix': [],
        'Steam': [],
        'Fortnite': [],
        'McDonalds': [],
        'Discord': [],
        'Xbox Live': [],
        'Pinterest': [],
        'Twitch': [],
        'Instagram': [],
        'LibreCraft': [],
        'Zoom': [],
        'Roblox': [],
        'MediaFire': [],
        'DeviantArt': [],
        'Aternos': [],
        'KFC': [],
        'BurgerKing': [],
        'EpicGames_Xbox': [],
        'Amazon': [],
        'EpicGames': [],
        'EpicGames_PSN': [],
        'Spotify': [],
        'UnknownCheats': [],
        'Activision': [],
        'FirstMail': [],
        'Kick': [],
        'AppleID': [],
        'BattleNet': [],
        'Restorecord': [],
        'NordVPN': [],
        'PayPal': [],
        'LeagueOfLegends': [],
        'Crunchyroll': [], 
        'Snapchat': [], 
    }

    for file_path in password_files:
        login_info = extract_login_info(file_path)
        for service in all_login_info:
            all_login_info[service].extend(login_info[service])

    save_login_info(results_dir, all_login_info)

if __name__ == '__main__':
    main()
