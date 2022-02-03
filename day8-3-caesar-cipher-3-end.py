alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#To improve encode and decode function merged as a function
def caesar(password_text, shift=3, direction="encode"):
    cipher_text = ""
    for letter in password_text:
        position = alphabet.index(letter)
        #加密
        if direction =="encode":
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        elif direction =="decode":
            new_position = position - shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    return cipher_text

if direction=="encode":
    encode_text = caesar(text,shift=5,direction="encode")
    print(f"The encoded text is {encode_text}")
elif direction =="decode":
    decode_text = caesar(text,shift=5,direction="decode")
    print(f"The decoded text is {decode_text}")