import socket
from cryptography.fernet import Fernet

def main():
    # Client setup
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))
    print("Connected to server.")

    # Receive the encryption key from the server
    try:
        key = client.recv(4096)
        cipher = Fernet(key)
    except Exception as e:
        print(f"Error receiving key: {e}")
        client.close()
        return

    while True:
        try:
            # Get user input
            message = input("Enter message (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break

            # Encrypt and send message
            encrypted_message = cipher.encrypt(message.encode('utf-8'))
            client.send(encrypted_message)

            # Receive and decrypt response
            encrypted_response = client.recv(4096)
            if not encrypted_response:
                print("Server disconnected.")
                break

            decrypted_response = cipher.decrypt(encrypted_response).decode('utf-8')
            print(f"Server response: {decrypted_response}")
        except ConnectionError as e:
            print(f"Connection error: {e}")
            break
        except Fernet.InvalidToken as e:
            print(f"Decryption error: {e}")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

    client.close()
    print("Disconnected from server.")

if __name__ == "__main__":
    main()