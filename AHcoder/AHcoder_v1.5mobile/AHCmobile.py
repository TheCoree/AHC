# AHcoder v1.5mobile   maked by corede

def coding(text, mixing, key):
    final = ""
    for i in text:
        coding_word = ord(i) + int(mixing)
        coded_word = str(coding_word) + str(key)
        final = final + chr(int(coded_word))
    print(final, end="")
    print(f"   mixing: {mixing}, key: {key}")

def decoder_main(text, mixing, key):
    text = text[:-20]
    message = ""
    for i in text:
        decoded = str(ord(i))
        decodedminone = decoded[:-1]
        final = int(decodedminone) - int(mixing)
        message = message + chr(int(final))
    print(message, end="")

def search_mix_and_key(text):
    key = None
    mixing = None
    for i in text[::-1]:
        if key is not None and mixing is not None:
            decoder_main(text, mixing, key)
            break
        elif i.isdigit() and key is None:
            key = i
        elif i.isdigit() and mixing is None:
            mixing = i

def start():
    print('''
   _____    ___ ___  _________  
  /  _  \  /   |   \ \_   ___ \ 
 /  /_\  \/    ~    \/    \  \/ 
/    |    \    Y    /\     \____
\____|__  /\___|_  /  \______  /
        \/       \/          \/  
 corede | type code for coding
   and decode for decoding\n''')
    while True:
        start = input(">>> ")
        if start == "code":
            text = input("\nEnter Text: ")
            mixing = input("Enter Mixing (min - 1, max - 9): ")
            key = input("Enter Key (min - 1, max - 9): ")
            coding(text, mixing, key)
        if start == "decode":
            text = input("\nEnter Text: ")
            search_mix_and_key(text)
        else:
            continue
start()
