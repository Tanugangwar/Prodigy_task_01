def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Choose (e)ncrypt or (d)ecrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice!")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted = encrypt(text, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = decrypt(text, shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
