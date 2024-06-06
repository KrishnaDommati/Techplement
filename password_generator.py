import random
import string
import argparse

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    if not (use_upper or use_lower or use_digits or use_special):
        raise ValueError("At least one character type must be selected")

    char_set = ''
    if use_upper:
        char_set += string.ascii_uppercase
    if use_lower:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    if use_special:
        char_set += string.punctuation

    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    password += random.choices(char_set, k=length - len(password))

    random.shuffle(password)

    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument('-l', '--length', type=int, required=True, help='Length of the password')
    parser.add_argument('-u', '--use_upper', action='store_true', help='Include uppercase letters')
    parser.add_argument('-lw', '--use_lower', action='store_true', help='Include lowercase letters')
    parser.add_argument('-d', '--use_digits', action='store_true', help='Include digits')
    parser.add_argument('-s', '--use_special', action='store_true', help='Include special characters')

    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.use_upper, args.use_lower, args.use_digits, args.use_special)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
