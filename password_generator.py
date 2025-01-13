import random
import string
import pyperclip

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if length < 1:
        print("Password length must be at least 1.")
        return ""
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Password Generator")
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    if password:
        print("\nGenerated Password:")
        print(password)
        copy_to_clipboard = input("\nCopy password to clipboard? (y/n): ").lower() == 'y'
        if copy_to_clipboard:
            pyperclip.copy(password)
            print("Password copied to clipboard!")