import requests
import random
import time
import os
from colorama import Fore

print(" tools dibuat ")


time.sleep(1)

import json

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

    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

    if response.status_code == 200:
        messages = response.json()
        if len(messages) == 0:
            break
        else:
            time.sleep(waktu1)

            message_id = messages[0]['id']
            response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
            if response.status_code == 204:
                print(Fore.GREEN + f'Pesan dengan ID {message_id} berhasil dihapus')
            else:
                print(Fore.RED + f'Gagal menghapus pesan dengan ID {message_id}: {response.status_code}')
    else:
        print(f'Gagal mendapatkan pesan di channel: {response.status_code}')

    # Lanjut ke pesan berikutnya
    i += 1
    if i >= len(words):  # kalau sudah sampai akhir file
        i = 0  # balik lagi ke awal

    time.sleep(waktu2)
