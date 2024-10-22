from cryptography.fernet import Fernet

def generate_key(filename='key.key'):
    key = Fernet.generate_key()
    with open(filename, 'wb') as key_file:
        key_file.write(key)
    print(f"Nyckel sparad till {filename}")

if __name__ == "__main__":
    generate_key()
