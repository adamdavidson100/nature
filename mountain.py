import numpy as np

def generate_key_matrix(key):
    n = int(len(key) ** 0.5)
    key_matrix = np.array([ord(char) - ord('A') for char in key.upper()])
    key_matrix = key_matrix.reshape((n, n))
    return key_matrix

def encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    plaintext = plaintext.upper().replace(" ", "")  # Convert to uppercase and remove spaces
    plaintext += 'X' * (n - (len(plaintext) % n))  # Pad plaintext if necessary
    ciphertext = ''
    for i in range(0, len(plaintext), n):
        block = np.array([ord(char) - ord('A') for char in plaintext[i:i+n]])
        block = block.reshape((n, 1))
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext += ''.join([chr(index + ord('A')) for index in encrypted_block.flatten()])
    return ciphertext

# Example usage:
# My plain text is whatever I send you as the encrypted message.
# I removed the key so only the ones I trust can understand my messages.
key_matrix = generate_key_matrix(key)
encrypted_text = encrypt(plaintext, key_matrix)
print("Encrypted text:", encrypted_text)
