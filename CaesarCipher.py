alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amt):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amt
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")


# Creating  a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amt):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_amt
            plain_text += alphabet[new_position]
        else:
            plain_text += letter
    print(f"The decoded text is {plain_text}")


# Start the loop to ask the user if they want to encode or decode
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift_num = int(input("Type the shift number:\n"))
    shift = shift_num % 26

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid option. Please type 'encode' or 'decode'.")

    # Asking the user if they want to go again
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != "yes":
        print("Goodbye!")
        break
