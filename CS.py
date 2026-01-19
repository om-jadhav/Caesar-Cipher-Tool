#!/usr/bin/env python3

import argparse
import os
import sys

# ================== COLORS ==================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ================== BANNER ==================
def hacker_banner():
    os.system("clear")
    print(CYAN + BOLD)
    print(" ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗ ")
    print("██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗")
    print("██║     ███████║█████╗  ███████╗███████║██████╔╝")
    print("██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗")
    print("╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║")
    print(" ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝")
    print(YELLOW + "        Caesar Cipher Attack Toolkit\n" + RESET)

# ================== CAESAR CORE ==================
def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.islower():
            base = 97
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)

        elif char.isupper():
            base = 65
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char

    return result

# ================== ENGLISH DETECTION ==================
COMMON_WORDS = [
    "the", "and", "is", "to", "of", "in", "that", "it", "for", "on", "with"
]

def english_score(text):
    score = 0
    text_lower = text.lower()

    for word in COMMON_WORDS:
        if word in text_lower:
            score += 5

    letters = sum(c.isalpha() for c in text)
    spaces = text.count(" ")

    if letters > 0:
        score += letters * 0.1
    score += spaces * 0.5

    return score

# ================== FILE HANDLING ==================
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(RED + f"❌ File not found: {filename}" + RESET)
        sys.exit(1)
    except PermissionError:
        print(RED + f"❌ Permission denied: {filename}" + RESET)
        sys.exit(1)

# ================== BRUTE FORCE ==================
def brute_force(text, auto_detect=False):
    print(BOLD + CYAN + "Brute-force results:\n" + RESET)

    results = []

    for shift in range(26):
        decrypted = caesar_cipher(text, shift, "decrypt")
        score = english_score(decrypted)
        results.append((shift, decrypted, score))

    results.sort(key=lambda x: x[2], reverse=True)

    for shift, decrypted, score in results:
        if auto_detect and score == results[0][2]:
            print(GREEN + BOLD + f"[LIKELY] Shift {shift:2}: {decrypted}" + RESET)
        else:
            print(YELLOW + f"Shift {shift:2}: {decrypted}" + RESET)

# ================== MAIN ==================
def main():
    hacker_banner()

    parser = argparse.ArgumentParser(
        description="Advanced Caesar Cipher Hacker Toolkit"
    )

    parser.add_argument(
        "mode",
        choices=["encrypt", "decrypt", "bruteforce"],
        help="Operation mode"
    )

    parser.add_argument(
        "message",
        nargs="?",
        help="Message text (ignored if -f is used)"
    )

    parser.add_argument(
        "shift",
        nargs="?",
        type=int,
        help="Shift value (required for encrypt/decrypt)"
    )

    parser.add_argument(
        "-f", "--file",
        help="Read input from file"
    )

    parser.add_argument(
        "--auto",
        action="store_true",
        help="Auto-detect English (bruteforce only)"
    )

    args = parser.parse_args()

    # Decide input source
    if args.file:
        text = read_file(args.file)
    elif args.message:
        text = args.message
    else:
        print(RED + "❌ Provide a message or use -f <file>" + RESET)
        sys.exit(1)

    if args.mode in ["encrypt", "decrypt"]:
        if args.shift is None:
            print(RED + "❌ Shift required for encrypt/decrypt" + RESET)
            sys.exit(1)

        shift = args.shift % 26
        result = caesar_cipher(text, shift, args.mode)

        print(GREEN + BOLD + "\nResult:\n" + RESET)
        print(CYAN + result + RESET)

    else:
        brute_force(text, auto_detect=args.auto)

# ================== ENTRY ==================
if __name__ == "__main__":
    main()
