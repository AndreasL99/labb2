import argparse
from cryptography.fernet import Fernet

def load_key(filename):
    with open(filename, 'rb') as key_file:
        return key_file.read()

def encrypt_file(key, filename):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        original_data = file.read()
    
    encrypted_data = f.encrypt(original_data)
    
    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    print(f"{filename} har blivit krypterad")

def decrypt_file(key, filename):
    f = Fernet(key)
    with open(filename, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    print(f"{filename} har blivit dekrypterad")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Krypteringsverktyg")
    parser.add_argument("operation", choices=["encrypt", "decrypt"], help="Välj: kryptera eller dekryptera")
    parser.add_argument("keyfile", help="Filen som innehåller krypteringsnyckeln")
    parser.add_argument("filename", help="Filen som ska krypteras eller dekrypteras")

    args = parser.parse_args()

    key = load_key(args.keyfile)

    if args.operation == "encrypt":
        encrypt_file(key, args.filename)
    elif args.operation == "decrypt":
        decrypt_file(key, args.filename)
