import hashlib
import bcrypt
import os

# Load plaintext passwords
with open("../passwords/original_passwords.txt", "r") as f:
    passwords = [line.strip() for line in f.readlines()]

# Ensure hashes directory exists
os.makedirs("../hashes", exist_ok=True)

# Open output files
with open("../hashes/md5_hashes.txt", "w") as md5_file, \
     open("../hashes/sha256_hashes.txt", "w") as sha256_file, \
     open("../hashes/bcrypt_hashes.txt", "w") as bcrypt_file:

    for password in passwords:
        md5_file.write(hashlib.md5(password.encode()).hexdigest() + "\n")
        sha256_file.write(hashlib.sha256(password.encode()).hexdigest() + "\n")
        bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        bcrypt_file.write(bcrypt_hash.decode() + "\n")

print("Hashes successfully written to /hashes/")

