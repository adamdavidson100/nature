import random

def generate_secret_message():
    # Define a list of words to use in the secret message
    words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", ".", "!", "?"]
    # Set the length of the secret message (you can adjust this as needed)
    message_length = random.randint(10, 20)
    # Randomly select words from the list to form the secret message
    secret_message = ' '.join(random.choices(words, k=message_length))
    return secret_message

# Example usage:
secret_message = generate_secret_message()
print("Generated secret message:", secret_message)
