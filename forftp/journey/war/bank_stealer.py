def simulate_cookie_dump():
    print("[*] Scanning Chrome localstorage...")
    print("[+] Grabbed session cookies: bank_session_abc123, credit_token_xyz456")
    print("[+] Sending to remote collector...")

def simulate_phishing():
    print("[*] Fake bank login served on local network.")
    print("[!] User credentials harvested: user@schoolmail.com / hunter2")

if __name__ == "__main__":
    simulate_cookie_dump()
    simulate_phishing()
