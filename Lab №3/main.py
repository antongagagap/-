import random
alphabet = 'abcdefghiklmnopqrstuvwxyz'

def read_file():
    text = ''
    with open('text.txt', 'r', encoding='utf8') as f:
        text = ''.join([line for line in f]).lower()
        text = text.replace('j', 'i')
    return text

text = read_file()

def generate_matrix():
    alphabet_indexes = list(range(len(alphabet)))
    random.shuffle(alphabet_indexes)
    key = ''.join([alphabet[i] for i in alphabet_indexes])
    key = [list(key[i:i+5]) for i in range(0, len(key), 5)]
    with open('key.txt', 'w', encoding='utf8') as f:
        for i in range(len(key)):
            for j in range(len(key[i])):
                f.write(f'{key[i][j]} - {i}, {j}\n')
    return key

key = generate_matrix()

matrixHeight = len(key)
matrixWidth = len(key[0])
 
def CryptoChar(char, cipher = True):
    for indexHeight in range(0, matrixHeight):
        for indexWidth in range(0, matrixWidth):
            if char == key[indexHeight][indexWidth]:
                if (cipher == True):
                    return key[(indexHeight + 1) % matrixHeight][indexWidth];
                else:
                    return key[(indexHeight - 1) % matrixHeight][indexWidth]
    return char;
    pass
 
 
def encryption(message):
    newMessage= ""
    for messageIndex in range(0, len(message)):
        newMessage += CryptoChar(message[messageIndex])
    return newMessage
 
def decryption(message):
    newMessage= ""
    for messageIndex in range(0, len(message)):
        newMessage += CryptoChar(message[messageIndex], False)
    return newMessage
 
def main():
    message = text
 
    cypherMessage = encryption(message)
    with open('encrypted_text.txt', 'w', encoding='utf8') as f:
        f.write(cypherMessage)
 
    decypherMessage = decryption(cypherMessage)
    with open('decrypter_text.txt', 'w', encoding='utf8') as f:
        f.write(decypherMessage)
    pass
 
if __name__ == "__main__":
    main()
