# keylogger_payload.py
# Used in Operation "Loose Keys"
# Note: Simulates keyboard capturing, logs to local file

import time

def simulate_keylogging():
    print("[*] Keylogger initialized.")
    keys = ["w", "e", "b", "c", "a", "m", "h", "a", "c", "k", "e", "d"]
    with open("keystrokes.log", "w") as f:
        for key in keys:
            f.write(f"{key}\n")
            time.sleep(0.3)
    print("[+] Keystrokes saved to keystrokes.log")

if __name__ == "__main__":
    simulate_keylogging()
