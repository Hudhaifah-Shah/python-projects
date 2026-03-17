alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
def eshift(shift):
    shifted_alpha = list(alphabet)
    shifted_letters = shifted_alpha[:shift]
    shifted_alpha = shifted_alpha[shift:] + shifted_letters
    return shifted_alpha
def encrypt(text):
    shifted_alpha = eshift(shift)
    enc_text = ""
    for i in text:
        if i in alphabet:
            ind = alphabet.index(i)
            enc_text += shifted_alpha[ind]
        else:
            enc_text += i
    print(f"Here is the encoded result: { enc_text }")
def decrypt(text):
    shifted_alpha = eshift(shift)
    dec_text = ""
    for i in text:
        if i in alphabet:
            ind = shifted_alpha.index(i)
            dec_text += alphabet[ind]
        else:
            dec_text += i
    print(f"Here is the decoded result: { dec_text }")
def caeser(dir):
    if dir == "encode":
        encrypt(text)
    elif dir == "decode":
        decrypt(text)
x = True
while x:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").strip().lower()
    text = input("Type your message: \n").strip().lower()
    shift = int(input("Type the shift number: \n"))
    caeser(direction)
    x = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").strip().lower()
    if x == "no": x = False
