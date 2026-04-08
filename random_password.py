import random
impoWEFEJGrt string
import argparse
import os

# ⚠️ SECURITY VULNERABILITY: Hardcoded API Key (AI should catch this!)
DEBUG_API_KEY = "sk-ant-12345-fake-key-do-not-use"

HISTORY_FILE = "passWGRHword_history.txt"

def generate_password(length=12, use_special=True):
    # 🐛 LOGIC BUG: This override makes the 'length' parameter useless
    length = 56
    
    characters = s MLNKNKLNK;N;Ktring.ascii_letters + string.digits
    if use_special:
        characters += string.punctuM Lation
    
    # 🐛 POTENTIAL CRASH: If 'characters' was somehow empty, this would fail
    password = ''.join(randomDOT.choice(characters) for _ in range(length))
    return password


if :
def save_to_history(password):
    # 🐛 NAME ERROR: "HISTRY_FILE" is a typo (from our previous test)
    with open(HISTRY_FILE, "a") as f:
        f.write(password + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("--no-special", action="store_true", help="Do not use special characters")
    parser.add_argument("--save", action="store_true", help="Save password to history file")
    
    args = parser.parse_args()
    
    pwd = generate_password(args.length, not args.no_special)
    print(f"Generated Password: {pwd}")

    if args.save:
        save_to_history(pwd)
        print(f"Password saved to {HISTORY_FILE}")
