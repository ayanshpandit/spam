import requests import time import os import threading from platform import system import socket import urllib.request

BOLD = '\033[1m' CYAN = '\033[96m'

logo = ("""\x1b[1;36m

\033[1;32m. /$$$$$$  /$$   /$$ /$$$$$$ /$$        /$$$$$$  /$$$$$$$  /$$      /$$ \033[1;34m. /$$__  $$| $$$ | $$|_  $$/| $$       /$$__  $$| $$__  $$| $$$    /$$$ \033[1;32m.| $$  \ $$| $$$$| $$  | $$  | $$      | $$  _/| $$  \ $$| $$$$  /$$$$ \033[1;34m.| $$$$$$$$| $$ $$ $$  | $$  | $$      |  $$$$$$ | $$$$$$$/| $$ $$/$$ $$ \033[1;32m.| $$__  $$| $$  $$$$  | $$  | $$       ____  $$| $$/ | $$  $$$| $$ \033[1;34m.| $$  | $$| $$\  $$$  | $$  | $$       /$$  \ $$| $$      | $$\  $ | $$ \033[1;32m.| $$  | $$| $$ \  $$ /$$$$$$| $$$$$$$$|  $$$$$$/| $$      | $$ /  | $$ \033[1;34m.|/  |/|__/  _/|/|/ _/ |/      |/     |__/

\033[1;32m  Developed by AYANSH (Messenger Tool with Auto-Resume on Network Reconnect) """)

def cls(): if system() == 'Linux': os.system('clear') elif system() == 'Windows': os.system('cls')

cls() print(logo)

def get_access_tokens(token_file): with open(token_file, 'r') as file: return [token.strip() for token in file.readlines() if token.strip()]

def is_connected(): try: urllib.request.urlopen('https://www.google.com', timeout=3) return True except: return False

def send_messages(convo_id, tokens, messages, custom_name, speed): headers = { 'Content-type': 'application/json', } while True: if is_connected(): try: for i, message in enumerate(messages): token = tokens[i % len(tokens)] full_message = f"{custom_name} {message.strip()}" url = f"https://graph.facebook.com/v17.0/t_{convo_id}" response = requests.post(url, json={"access_token": token, "message": full_message}, headers=headers) current_time = time.strftime("%Y-%m-%d %I:%M:%S %p") if response.ok: print(f"\033[1;32m[SENT] {full_message}  | Time: {current_time}") else: print(f"\033[1;31m[FAILED] Token Error or Limit | Time: {current_time}") time.sleep(speed) print("\033[1;33m[+] Loop completed. Restarting...") except Exception as e: print(f"\033[1;31m[!] Exception: {e}") else: print("\033[1;34m[!] No Internet. Sleeping...") while not is_connected(): time.sleep(5) print("\033[1;32m[+] Internet Back. Resuming...")

def main(): token_file = input(BOLD + CYAN + "Token File Path => ").strip() convo_id = input(BOLD + CYAN + "Conversation ID => ").strip() messages_file = input(BOLD + CYAN + "Messages File Path => ").strip() custom_name = input(BOLD + CYAN + "Custom Name Prefix => ").strip() speed = int(input(BOLD + CYAN + "Delay Between Messages (sec) => ").strip())

tokens = get_access_tokens(token_file)
with open(messages_file, 'r') as f:
    messages = f.readlines()

send_messages(convo_id, tokens, messages, custom_name, speed)

if name == 'main': main()
