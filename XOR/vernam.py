from os import urandom

def genkey(length):
    return bytearray(urandom(length))

def vernam(text, key):
    return bytearray([text[i] ^ key[i]
     for i in range(len(text))
     ])

plaintext = bytearray('Missatge original', 'UTF-8')
key = genkey(len(plaintext))
print('Text pla: ' + str(plaintext))
ciphertext = vernam(plaintext, key)
print('Text xifrat: ' + str(ciphertext))
plaintext2 = vernam(ciphertext, key)
print('Text desxifrat: ' + str(plaintext2))
