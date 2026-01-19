# 🔐 Caesar Hacker  
### Caesar Cipher Encryption & Attack Toolkit

**Caesar Hacker** is a Linux-based **Python CLI tool** that implements **Caesar cipher encryption, decryption, brute-force attacks, and automatic English detection**.

This project is built for **learning cryptography fundamentals, classical cipher weaknesses, and real-world cryptanalysis techniques**.

---

## ✨ Features

- 🔒 Encrypt text using Caesar Cipher
- 🔓 Decrypt text with a known shift
- 💣 Brute-force all 26 shifts
- 🧠 Auto-detect English plaintext
- 📂 File input support (`-f <file>`)
- 🎨 Colored terminal output
- 😈 Hacker-style ASCII banner
- 🐧 Linux executable script
- ⚡ No external dependencies

---

## 🧠 What is Caesar Cipher?

The Caesar cipher is a classical substitution cipher where each letter is shifted by a fixed number of positions.

Example (shift = 3):

A → D
B → E
Z → C

yaml
Copy code

---

## 📦 Requirements

- Python 3.7 or higher
- Linux / WSL / Unix-based terminal

---

## ⚙️ Installation

### 1️⃣ Clone the repository

git clone https://github.com/yourusername/Caesar-Cipher-Tool.git
### 2️⃣ Navigate into the project directory
cd Caesar-Cipher-Tool
### 3️⃣ Make the script executable
chmod +x CS.py
### 4️⃣ Verify installation
./CS.py --help
## 🖥 Usage
General Syntax
./CS.py <mode> [options] <shift>
## 🔒 Encrypt Mode
./CS.py encrypt "HELLO WORLD" 3
./CS.py encrypt -f plain.txt 5
## 🔓 Decrypt Mode
./CS.py decrypt "KHOOR ZRUOG" 3
./CS.py decrypt -f encrypted.txt 3
## 💣 Brute-force Mode
./CS.py bruteforce -f encrypted.txt
## 🧠 Auto-Detect Mode
./CS.py bruteforce -f encrypted.txt --auto
## 📌 Command Summary
Mode	Shift Required	Description
encrypt	Yes	Encrypt plaintext
decrypt	Yes	Decrypt ciphertext
bruteforce	No	Try all shifts
bruteforce --auto	No	Auto-detect plaintext

##🧪 Example
Encrypted text:

objectivec
Copy code
WKLV LV D VHFUHW PHVVDJH
Output:


[+] Shift 3 → THIS IS A SECRET MESSAGE
## 🧠 How It Works
Caesar cipher shifts characters within the alphabet

Brute-force tests all 26 keys

English scoring ranks results using word and space frequency

## 📁 Project Structure

Caesar-Cipher-Tool/
├── CS.py
├── encrypted.txt
└── README.md
## ⚠️ Disclaimer
This project is for educational purposes only.
Do not use Caesar cipher for real-world security.

## 👤 Author
Om Jadhav
Computer Engineering Student
Cybersecurity Enthusiast

## ⭐ Support
If you found this useful, give the repository a ⭐
