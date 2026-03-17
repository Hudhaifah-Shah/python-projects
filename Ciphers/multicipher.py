alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
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
def caeser(dir):
    if dir == "encode":
        encrypt(text, shift)
    elif dir == "decode":
        decrypt(text, shift)
x = True
while x:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").strip().lower()
    text = input("Type your message: \n").strip().lower()
    shift = int(input("Type the shift number: \n"))
    caeser(direction)
    x = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").strip().lower()
    if x == "no": x = False
