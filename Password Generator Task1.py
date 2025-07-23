import random
import string

def generate_password(length):
    """Generate a random password with given length."""
    # Combine all character sets for complexity
    characters = string.ascii_letters + string.digits + string.punctuation
    # Ensure at least one character from each set for stronger passwords
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    # Fill the rest with random choices
    password += random.choices(characters, k=length-4)
    # Shuffle to avoid predictable order
    random.shuffle(password)
    return ''.join(password)

# User input for desired password length
while True:
    try:
        length = int(input("Enter desired password length (minimum 4): "))
        if length < 4:
            print("Password must be at least 4 characters long.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Generate and display the password
password = generate_password(length)
print("Generated Password:", password)

