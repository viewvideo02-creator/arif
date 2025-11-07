import requests
import random
import time
import os
from colorama import Fore
import json

print(" tools dibuat ")

time.sleep(1)

with open("config.json", "r") as f:
    config = json.load(f)

channel_id = config["channel_id"]
waktu1 = config["delay_delete"]
waktu2 = config["delay_send"]

print("[INFO] Setting Bot:")
time.sleep(1)
print(f"  Channel ID   : {channel_id}")
time.sleep(1)
print(f"  Hapus tiap   : {waktu1} detik")
time.sleep(1)
print(f"  Kirim tiap   : {waktu2} detik")

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

with open("pesan.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

i = 0
while True:
    channel_id = channel_id.strip()

    payload = {
        'content': words[i].strip()
    }

    headers = {
        'Authorization': authorization
    }

    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
    print(Fore.WHITE + "Sent message: ")
    print(Fore.YELLOW + payload['content'])

    if r.status_code == 200 or r.status_code == 201:
        message_id = r.json()["id"]
    else:
        print(Fore.RED + f"Gagal mengirim pesan (status {r.status_code}), skip hapus.")
        time.sleep(waktu2)
        i += 1
        if i >= len(words):
            i = 0
        continue

    time.sleep(waktu1)

    delete = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}", headers=headers)
    if delete.status_code == 204:
        print(Fore.GREEN + f'Pesan dengan ID {message_id} berhasil dihapus')
    else:
        print(Fore.RED + f'Gagal menghapus pesan dengan ID {message_id}: {delete.status_code}')

    i += 1
    if i >= len(words):
        i = 0

    time.sleep(waktu2)
