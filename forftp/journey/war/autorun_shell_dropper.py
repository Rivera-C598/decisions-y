# autorun_shell_dropper.py
# Dropped via USB, opens reverse shell on unsuspecting system

import os
import time

def fake_reverse_shell():
    print("[*] Executing reverse shell payload...")
    time.sleep(1)
    print("[*] Connecting to 172.20.10.5:4444...")
    time.sleep(1)
    print("[!] Shell established. Remote access granted.")
    print("[+] Commands being executed...")

if __name__ == "__main__":
    fake_reverse_shell()
