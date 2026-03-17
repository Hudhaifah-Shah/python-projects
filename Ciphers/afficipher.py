alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
def encrypt(text, a, b):
    enc_text = "" 
    for i in text: 
        if i in alphabet:
            ind = (alphabet.index(i) * a) + b  
            ind %= len(alphabet) 
            enc_text += alphabet[ind] 
        else: 
            enc_text += i
    print(f"Here is the encoded result: { enc_text }")
def decrypt(text, a, b):
    dec_text = "" 
    a = pow(a, -1, 26)
    for i in text: 
        if i in alphabet:
            ind = (alphabet.index(i) - b) * a
            ind %= len(alphabet) 
            dec_text += alphabet[ind] 
        else: 
            dec_text += i
    print(f"Here is the decoded result: { dec_text }")
def caeser(dir):
    if dir == "encode":
        encrypt(text, akey, bkey) 
    elif dir == "decode": 
        decrypt(text, akey, bkey) 
x = True  
while x: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").strip().lower()
    text = input("Type your message: \n").strip().lower()
    akey = int(input("Type the key a: \n"))
    bkey = int(input("Type the key b: \n"))
    caeser(direction)
    x = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").strip().lower()
    if x == "no": x = False
