def caesar_encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Algorithm:-")
    while True:
        attempts = 0

        while attempts < 3:
            choice = input("Do you want to encrypt(e) or decrypt(d)? ").lower()

            if choice not in ['e', 'd']:
                print("Invalid choice! Enter a valid one.")
                attempts += 1
                if attempts == 3:
                    quit_choice = input("Do you want to quit (yes/no)? ").lower()
                    if quit_choice == 'yes':
                        print("Exiting program.")
                        return
                    elif quit_choice == 'no':
                        attempts = 0
                    else:
                        print("Invalid choice! Exiting program.")
                        return
            else:
                break

        if attempts == 3:
            print("You've exceeded the maximum number of attempts. Exiting program.")
            return

        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            encrypted_message = caesar_encrypt(message, shift)
            print("Encrypted Message:", encrypted_message)
        elif choice == 'd':
            decrypted_message = caesar_decrypt(message, shift)
            print("Decrypted Message:", decrypted_message)

        another = input("Do you want to encrypt or decrypt another text? (yes/no) ").lower()
        if another != 'yes':
            print("Exiting program.")
            return

if __name__ == "__main__":
    main()
