alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
text = input("Type your message: \n").strip().lower()

def encrypt(text, shift):
    enc_text = ""
    for i in text:
        if i in alphabet:
            ind = alphabet.index(i) + shift
            ind %= len(alphabet)
            enc_text += alphabet[ind]
        else:
            enc_text += i
    print(f"Here is the encoded result: { enc_text }")
def decrypt(text, shift):
    dec_text = ""
    for i in text:
        if i in alphabet:
            ind = alphabet.index(i) - shift
            ind %= len(alphabet)
            dec_text += alphabet[ind]
        else:
            dec_text += i
    print(f"Here is the decoded result: { dec_text }")

for _ in range(1, 27):
    decrypt(text, _)
