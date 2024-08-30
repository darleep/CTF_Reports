from Crypto.Cipher import AES
 from Crypto.Util.Padding import unpad
 import os
 import sys
 def decrypt_file(input_path, output_path, key, iv):
    try:
        key = key.encode('utf-8')
        iv = iv.encode('utf-8')
        # Read the encrypted file
        with open(input_path, 'rb') as file:
            encrypted_data = file.read()
        # Create AES cipher object for decryption
        cipher = AES.new(key, AES.MODE_CBC, iv)
 5
 Chrome Room - TryHackMe
        # Decrypt the data
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        # Write the decrypted data to the output file
        with open(output_path, 'wb') as file:
            file.write(decrypted_data)
        print("File decrypted and saved successfully.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except ValueError as ve:
        print(f"Decryption error: {ve}")
    except Exception as ex:
        print(f"An error occurred: {ex}")
 def main():
    if len(sys.argv) !=5:
        print("Usage: python decryptor.py <key> <iv> <input_file> <output_file>")
        sys.exit(1)
    # Define key and IV (Initialization Vector)
    key = sys.argv[1]
    iv = sys.argv[2]
    # Paths to the encrypted and decrypted files
    encrypted_file_path = sys.argv[3]
    decrypted_file_path = sys.argv[4]
    # Decrypt the file
    decrypt_file(encrypted_file_path, decrypted_file_path, key, iv)
 if __name__ == "__main__":
    main()
