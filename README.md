# Password-Cracking

An ethical cybersecurity lab project that demonstrates how different password hashing algorithms (MD5, SHA256, bcrypt) fall to cracking attempts using real tools and real, weak passwords.

---

## Overview

Password-Cracking simulates a controlled password attack environment using **John the Ripper** and custom Python scripts. It demonstrates the real-world risk of weak passwords and evaluates the effectiveness of popular hashing algorithms.

---

## Features

- Generate password hashes using:
  - `MD5`
  - `SHA256`
  - `bcrypt` 
- Crack hashed passwords using:
  - **John the Ripper**
  - Dictionary/wordlist attacks
- Log and compare cracking speeds
- Evaluate hash strength vs weak passwords
- Document all results with markdown and logs

---

## Tech Stack

- **Languages**: Python, Bash, Markdown
- **Hashing**: `hashlib`, `bcrypt`
- **Cracking Tool**: John the Ripper
- **Data**: Custom wordlists, sample password files
- **Logging**: Command output + benchmarking summaries

---

## How to Run

### 1. Set Up Environment
- Install Python
- Install `bcrypt` module:
```bash
    pip install bcrypt
### 2. Generate Hashes
From the scrips/ folder:
```bash
    python generate_hashes.py
### 3. Crack Hashes with John
From John's /run/ folder:
```bash
   # Crack MD5 hashes
john.exe --format=raw-md5 --wordlist=my_wordlist.txt md5_hashes.txt

# Crack SHA256 hashes
john.exe --format=raw-sha256 --wordlist=my_wordlist.txt sha256_hashes.txt

# Crack bcrypt hashes (slow!)
john.exe --format=bcrypt --wordlist=my_wordlist.txt bcrypt_hashes.txt
 
##  Screenshots


##  Future Work
-Automate cracking + result logging with Python
-Add hash benchmarking script with visual graphs
-Explore GPU cracking with Hashcat
