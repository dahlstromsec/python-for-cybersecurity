#!/usr/bin/env python3

"""
Hash Identifier
Version: 1.0

Identifies common hash algorithms based on hash length
and basic format validation.

Author: dahlstromsec
"""

import re


def is_hexadecimal(value):
    """Return True if the string contains only hexadecimal characters."""
    return bool(re.fullmatch(r"[0-9a-fA-F]+", value))


def identify_hash(hash_value):
    """Identify possible hash types."""

    length = len(hash_value)
    possibilities = []

    if length == 32 and is_hexadecimal(hash_value):
        possibilities.extend([
            "MD5",
            "NTLM",
            "LM"
        ])

    elif length == 40 and is_hexadecimal(hash_value):
        possibilities.append("SHA-1")

    elif length == 56 and is_hexadecimal(hash_value):
        possibilities.append("SHA-224")

    elif length == 64 and is_hexadecimal(hash_value):
        possibilities.append("SHA-256")

    elif length == 96 and is_hexadecimal(hash_value):
        possibilities.append("SHA-384")

    elif length == 128 and is_hexadecimal(hash_value):
        possibilities.append("SHA-512")

    elif length == 60 and hash_value.startswith("$2"):
        possibilities.append("bcrypt")

    return possibilities


def main():

    print("=" * 50)
    print(" Hash Identifier v1.0")
    print("=" * 50)

    while True:

        print("\nType 'exit' to quit.")

        user_hash = input("\nEnter hash: ").strip()

        if user_hash.lower() == "exit":
            print("\nGoodbye!")
            break

        matches = identify_hash(user_hash)

        if not matches:
            print("\nNo matching hash type found.")

        elif len(matches) == 1:
            print("\nPossible hash type:")
            print(f" - {matches[0]}")

        else:
            print("\nPossible hash types:")

            for item in matches:
                print(f" - {item}")

            print("\nNote:")
            print("Some algorithms share the same output length.")
            print("Additional context is required for a definitive identification.")


if __name__ == "__main__":
    main()
