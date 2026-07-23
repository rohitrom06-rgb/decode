"""
DecodeLabs — Random Password Generator
========================================
Key Skill: Randomization & String manipulation.

Why it matters: Secure password generation is a common backend
requirement -- combining character sets, controlling length, and
using a cryptographically safe random source.
"""

import random
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Builds a random password from the selected character pools."""
    pool = string.ascii_lowercase  # always include lowercase letters

    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # random.choices allows repeats, which is standard for password generation
    password = "".join(random.choices(pool, k=length))
    return password


def get_int_input(prompt, default):
    """Reads an integer from the user, falling back to a default."""
    raw = input(prompt).strip()
    if raw == "":
        return default
    try:
        return int(raw)
    except ValueError:
        print(f" -> Invalid number, using default ({default}).")
        return default


def get_yes_no_input(prompt, default=True):
    """Reads a yes/no answer from the user, falling back to a default."""
    raw = input(prompt).strip().lower()
    if raw == "":
        return default
    return raw in ("y", "yes")


def main():
    print("----- DecodeLabs Random Password Generator -----\n")

    length = get_int_input("Password length (default 12): ", 12)
    use_upper = get_yes_no_input("Include uppercase letters? (Y/n): ", True)
    use_digits = get_yes_no_input("Include digits? (Y/n): ", True)
    use_symbols = get_yes_no_input("Include symbols? (Y/n): ", True)

    password = generate_password(length, use_upper, use_digits, use_symbols)

    print("\n--------------------------------------")
    print(f"Generated Password: {password}")
    print("--------------------------------------")


if __name__ == "__main__":
    main()