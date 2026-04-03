import random
import string
import argparse
import os

HISTORY_FILE = "password_history.txt"

def generate_password(length=12, use_special=True):
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_to_history(password):
    # Potential improvement: Use a more secure storage or a database
    with open(HISTORY_FILE, "a") as f:
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
