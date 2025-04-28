import socket
import threading
from cryptography.fernet import Fernet

# Generate a Fernet key (in a real system, this should be securely shared with clients)
key = Fernet.generate_key()
cipher = Fernet(key)

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address} established.")

    # Send the encryption key to the client (for simplicity; in production, use secure key exchange)
    try:
        client_socket.send(key)
    except Exception as e:
        print(f"Error sending key to {client_address}: {e}")
        client_socket.close()
        return

    while True:
        try:
            # Receive encrypted data
            encrypted_data = client_socket.recv(4096)
            if not encrypted_data:
                break

            # Decrypt the data
            decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
            print(f"Received from {client_address}: {decrypted_data}")

            # Encrypt and send response
            response = f"Echo: {decrypted_data}"
            encrypted_response = cipher.encrypt(response.encode('utf-8'))
            client_socket.send(encrypted_response)
        except ConnectionError as e:
            print(f"Connection error with {client_address}: {e}")
            break
        except Fernet.InvalidToken as e:
            print(f"Decryption error with {client_address}: {e}")
            break
        except Exception as e:
            print(f"Unexpected error with {client_address}: {e}")
            break

    print(f"Connection from {client_address} closed.")
    client_socket.close()


def main():
    # Server setup
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)
    print("Server listening on port 12345...")

    while True:
        try:
            client_socket, client_address = server.accept()
            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            break
        except Exception as e:
            print(f"Server error: {e}")

    server.close()


if __name__ == "__main__":
    main()