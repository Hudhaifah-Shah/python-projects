alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
text = input("Type your message: \n").strip().lower()

def encrypt(text, shift):
    enc_text = ""
    for i in text:
        if i in alphabet:
            ind = alphabet.index(i) * shift
            ind %= len(alphabet)
            enc_text += alphabet[ind]
        else:
            enc_text += i
    print(f"Here is the encoded result: { enc_text }")
def decrypt(text, shift):
    dec_text = ""
    shift = pow(shift, -1, 26)
    for i in text:
        if i in alphabet:
            ind = alphabet.index(i) * shift
            ind %= len(alphabet)
            dec_text += alphabet[ind]
        else:
            dec_text += i
    print(f"Here is the decoded result: { dec_text }")
keys = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
for _ in keys:
    decrypt(text, _)
