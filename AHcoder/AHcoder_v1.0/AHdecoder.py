# AHcoder v1.0   maked by corede

def decoder_main(text, mixing, key):
    text = text[:-20]
    message = ""
    for i in text:
        decoded = str(ord(i))
        decodedminone = decoded[:-1]
        final = int(decodedminone) - int(mixing)
        message = chr(int(final))
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
    while True:
        text = input("\nEnter Text: ")
        search_mix_and_key(text)

start()