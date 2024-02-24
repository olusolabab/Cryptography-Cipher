import string


def caeserEncrypt(message, key):

    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    encryptedMessage = message.lower().translate(cipher)
    return encryptedMessage


def caeserDecrypt(encryptedMessage, key):

    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    message = encryptedMessage.translate(cipher)
    return message


message = input("Enter the message: ")
key = int(input("Enter the key: "))


encryptedMessage = caeserEncrypt(message, key)
print(f"Encrypted message: {encryptedMessage}")

decryptedMessage = caeserDecrypt(encryptedMessage, key)
print(f"Decrypted message: {decryptedMessage}")