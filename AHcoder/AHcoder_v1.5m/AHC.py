# AHcoder v1.5m   maked by corede

def file_write(text):
    with open("coded.txt", "a") as file:
        file.write(text + '\n')

def coding(text, mixing, key):
    final = ""
    for i in text:
        coding_word = ord(i) + int(mixing)
        coded_word = str(coding_word) + str(key)
        final = final + chr(int(coded_word))
    print(final, end="")
    print(f"   mixing: {mixing}, key: {key}")
    file_write(text + " -> " + final)

def decoder_main(text, mixing, key):
    text = text[:-20]
    message = ""
    for i in text:
        decoded = str(ord(i))
        decodedminone = decoded[:-1]
        final = int(decodedminone) - int(mixing)
        message = message + chr(int(final))
    print(message, end="" + "\n")
    file_write(text + " -> " + message)
    

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
░▒▓██████▓▒░░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░░▒▒▒░░        
░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░░░░░░░       
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░░▒▒▒░░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░  
    maker corede | type code for coding
        and decode for decoding''')
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
