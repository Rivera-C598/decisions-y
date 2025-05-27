import time
import random
import sys

def type_writer(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch(text, cycles=3):
    for _ in range(cycles):
        glitched = ''.join(random.choice("█▒░ ") for _ in text)
        sys.stdout.write("\r" + glitched)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + text + "\n")
    sys.stdout.flush()

random_responses = [
    "You don’t get it yet, do you??",
    "Wrong question. Try again.",
    "You’re asking the wrong things...",
    "???",
    "I won’t answer that. Ask better..."
]

questions = {
    "who are you?": "They call me cisco, sound famillar? hahahahh lol look at me, sounding like im sort of a big time hacker. pfft",
    "what is this?": "This is for you. You’re the one sent to follow me, right?? youre nexabank's cybersecurity recruits.\nits obvious they're gonna send someone after me, cuz I was about to sink them.",
    "why did you do it?": "Why does anyone do anything? I was buried in ₱38,000 debt that turned into ₱126,000 overnight, hows that make you feel? I was desperate.",
    "what do you want?": "I just want peace, but now I want justice. But I'll get there, one leak at a time. or I wont.",
    "what did you find?": "Enough to sink nexabank. the hidden charges. altered logs. and secret scripts to bleed us students dry.",
    "where is the evidence?": "All packed in a nice directory at /smb/bag/",
    "...": "hard to believe huh? but this is the truth, believe me I've reported this to the authorities\nbut it seems like they dont want to deal with nexabank itself, its as if nexabank owns them.",
    "and then?": "thats why Ive resorted to hacking them, I have also created a blog site to expose their atrocities, but was interrupted. I was about to upload all evidence there\nyou can check it out on http://192.168.56.143/unleash/thetruth/nexabankfiles",
    "how can i trust you?": "You can’t. That’s the fun part. But you’ll see soon enough what’s real and what’s not.",
    "i believe you": "are you sure? this could make you lose your job. nexabank will find you, you'd become a criminal like me.",
    "not if im good enough": "Damn.",
    "so where do i go next?": "SSH into my machine: 192.168.56.143 | user: francisco_shaw | pass: cisco209347\nFind nexabank's website ip address in a textfile called access.txt\nI know nexabank's website as well as the only vulnerable page they have that will only last for a limited time.\nexploiting this page will be our only chance to clear all student debt.",
    "we'll delete all student debt?": "Yes and I know just how.",
    "how?": "Through nexabank's testing site, here they test file uploads, sql queries, and cmd execution\nI can tell this is where they upload their scripts to add hidden charges to all student debt.",  
    "okay, then what?": "upload a reverse shell malware and execute it via remote code execution.\nOnce youre in, upgrade to root access: you can use the access code they used as a placeholder for the testing site as the password for root\nrun mysql -u root -p and delete student_debt table.",
    "great, i have gathered a ton of info about you today": "... thats",
    "your current plan, nexabank's only vulnerability": "...",
    "what if i just hand you over to nexabank?": "... you ...",
    "fill my status quo of catching you": "......",
    "what now?": "Now you decide. Obey the bank and shut me down... or finish what I started."
}

asked = set()

type_writer("Activation sequence:376eb activated. ask away...\n")

try:
    while True:
        inp = input("> ").strip().lower()

        if inp in ["exit", "quit"]:
            type_writer("Exiting chatbot... Goodbye.", delay=0.02)
            break

        if inp in questions:
            if inp in asked:
                type_writer("You’ve already asked that. Ask the next question.")
            else:
                if inp == "what now?":
                    glitch(questions[inp])
                else:
                    type_writer(questions[inp], delay=0.04)
                asked.add(inp)
        else:
            type_writer(random.choice(random_responses), delay=0.03)

        if len(asked) == len(questions):
            type_writer("\n✅ You’ve asked the right questions. The truth is now yours.\n", delay=0.02)
            break
except KeyboardInterrupt:
    print("\nChatbot terminated.")
