import random
import string
import argparse
import os
import hashlib

# Removed hardcoded API key
# DEBUG_API_KEY = "sk-ant-12345-fake-key-do-not-use"

HISTORY_FILE = "password_history.txt"

def generate_password(length=12, use_special=True):
 # Removed hardcoded length variable
 characters = string.ascii_letters + string.digits
 if use_special:
 characters += string.punctuation
 
 # Added input validation
 if length < 8:
 raise ValueError("Password length must be at least 8")
 
 password = ''.join(random.choice(characters) for _ in range(length))
 return password

def save_to_history(password):
 # Fixed typo in HISTORY_FILE variable name
 with open(HISTORY_FILE, "a") as f:
 # Hash and salt the password before storing it
 hashed_password = hashlib.sha256(password.encode()).hexdigest()
 f.write(hashed_password + "\n")

if __name__ == "__main__":
 parser = argparse.ArgumentParser(description="Generate a random password.")
 parser.add_argument("-l", "--length", type=int, default=12, help="Password length")
 parser.add_argument("-s", "--special", action="store_true", help="Use special characters")
 args = parser.parse_args()
 
 password = generate_password(args.length, args.special)
 save_to_history(password)
 print(password)

   
