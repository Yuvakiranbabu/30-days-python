def encrypt(text, key):
    encrypted_text = ""  # Store encrypted message
    key_len = len(key)  # Length of key

    for i, char in enumerate(text):
        if char.isalpha():  # Only encrypt letters (A-Z, a-z)
            shift = key[i % key_len]  # Get shift value from key
            base = ord('A') if char.isupper() else ord('a')  # Find base (uppercase/lowercase)
            new_char = chr((ord(char) - base + shift) % 26 + base)  # Shift and wrap around
            encrypted_text += new_char
        else:
            encrypted_text += char  # Keep non-letters the same
    
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""  # Store decrypted message
    key_len = len(key)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = key[i % key_len]  # Get shift value from key
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - shift) % 26 + base)  # Reverse the shift
            decrypted_text += new_char
        else:
            decrypted_text += char
    
    return decrypted_text

# Example
key = [3, 1, 4, 2]  # Key pattern
plaintext = "I am ted mosby"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted_text}")
