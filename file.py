def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Program")
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' or 'd'.")
        return

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid input. Shift value must be an integer.")
        return

    if choice == 'e':
        result = caesar_cipher_encrypt(text, shift)
        print(f"Encrypted Message: {result}")
    elif choice == 'd':
        result = caesar_cipher_decrypt(text, shift)
        print(f"Decrypted Message: {result}")

if __name__ == "__main__":
    main()
