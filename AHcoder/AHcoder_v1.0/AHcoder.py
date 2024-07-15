# AHcoder v1.0   maked by corede

def coding(text, mixing, key):
    for i in text:
        coding_word = ord(i) + int(mixing)
        coded_word = str(coding_word) + str(key)
        final = chr(int(coded_word))
        print(final, end="")
    print(f"   mixing: {mixing}, key: {key}")

def start():
    while True:
        text = input("\nEnter Text: ")
        mixing = input("Enter Mixing (min - 1, max - 9): ")
        key = input("Enter Key (min - 1, max - 9): ")
        coding(text, mixing, key)
        
start()
