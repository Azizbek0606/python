message = input("Enter your message: ")
shift = int(input("Enter the shift value (1-25): "))
encrypted_message = ""

for char in message:
    if char.isalpha():
        if char.islower():
            new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        encrypted_message += new_char
    else:
        encrypted_message += char
print("Encrypted message:", encrypted_message)
