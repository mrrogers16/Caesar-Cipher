import base64


def encrypt_message(plaintext_message, key):
    # Initialize empty bytearray to ensure all characters, including non-printable ones, are handeled
    encrypted_bytes = bytearray()
    ascii_codes = []
    key_length = len(key)

    for i in range(len(plaintext_message)):
        # Convert plaintext message character to its ASCII value
        # ord function converts character to its ASCII value
        message_char = ord(plaintext_message[i])

        # Use the mod operator to cycle through key for the length of the plaintext message
        key_char = ord(key[i % key_length])

        # Add ASCII value of the message and the key character and then mod 255 rto avoid overflow
        encrypted_char = (message_char + key_char) % 255
        """
        The code below initially appended the encrypted character directly to the string resulting in unprintable characters to cause issues with my terminal.
            # Append encrypted character to the string encrypted_message
            # chr function converts ASCII value back to its character, opposite of ord function
            encrypted_message += chr(encrypted_char)

            # Store the encrypted character's ASCII value as a string for later output
            ascii_codes.append(str(encrypted_char))
        """

        # Append encrypted_char to bytearray
        encrypted_bytes.append(encrypted_char)

        # Convert ASCII Value to string to ensure printability and then append it to the ascii_codes array
        ascii_codes.append(str(encrypted_char))

    return encrypted_bytes, "-".join(ascii_codes)


def decrypt_message(encrypted_bytes, key):
    decrypted_message = ""
    key_length = len(key)

    for i in range(len(encrypted_bytes)):
        # Get ASCII value of encrypted character
        encrypted_char = encrypted_bytes[i]
        # Get corresponding key character and cycle through key using mod
        key_char = ord(key[i % key_length])
        # Subtract the key's ASCII value from the encrypted character and then mod 255 to avoid overflow
        decrypted_char = (encrypted_char - key_char) % 255
        # Append decrypted character to the string decrypted message
        decrypted_message += chr(decrypted_char)

    return decrypted_message


def format_output(plaintext_message, key):
    # Call encrypt
    encrypted_bytes, ascii_codes = encrypt_message(plaintext_message, key)
    """
        NOTE: To ensure reliable printing to the console, the encrypted bytearray is base46 encoded. This ensures that any non-printable characters are represented in a human readable format
        We then decode it into a utf-8 string for display. I was able to get output matching the instructions pdf. I have just modified the program to handle non-printable characters
        because they keep causing my terminal to crash. 
    """

    encrypted_message_b64 = base64.b64encode(encrypted_bytes).decode("utf-8")
    # Call decrypt
    decrypted_message = decrypt_message(encrypted_bytes, key)

    # Format output
    print(f"\nOriginal Message: {plaintext_message}")
    print(f"Key: {key}")
    print(f"Cipher Text: {encrypted_message_b64}")
    print(f"Cipher Text ASCII: {ascii_codes}")
    print(f"Deciphered Text: {decrypted_message}")


def main():
    """
    Please read multiline comments. I tried to print the ascii values to the console normally.
    It kept breaking my terminal. The code to print these values remains and is commented out inside of the encrypt function.
    """

    # Take in the message from user
    plaintext_message = input("Enter the plaintext message: ")
    # Take in the key from user
    key = input("Enter the key: ")

    # Call format output function to start everything
    format_output(plaintext_message, key)


if __name__ == "__main__":
    main()
