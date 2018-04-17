plain = input("Input text to be encrypted or decrypted: ")

def f(x):
    cipher_text = ''
    for i in x:
        if i != " ":
            cipher_text += (chr(-ord(i) + 219))
        elif i == ' ':
            cipher_text += ' '
    print(cipher_text)

f(plain)
