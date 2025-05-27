# builder.py
# Malware Customizer v1.6

import time
import random

templates = [
    "ReverseShellGen", 
    "WiFiSnifferX", 
    "KeyloggerPlus", 
    "USBInfector", 
    "BrowserCookieDumper"
]

def fake_build(payload_name):
    print(f"[*] Initializing malware builder: {payload_name}")
    time.sleep(1)
    print("[*] Generating obfuscated payload...")
    time.sleep(1)
    print("[*] Encrypting strings and adding junk code...")
    time.sleep(1)
    print(f"[+] Payload '{payload_name}_final.py' successfully created!")
    print("[!] Upload to USB or serve via phishing link.")
    print("[*] You know what to do...")

def menu():
    print("=== Cisco's Malware Builder v1.0 ===")
    print("Available Templates:")
    for i, t in enumerate(templates, 1):
        print(f"  [{i}] {t}")
    
    choice = input("\nSelect a payload to build (1-5): ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(templates):
            fake_build(templates[index])
        else:
            print("Invalid choice.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    menu()
