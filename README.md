# AHC - ASCII Hyper Coder v1.5m User Guide

## Introduction
AHC - ASCII Hyper Coder is a medium-complexity encryption tool that converts text into encrypted form using ASCII values. This tool mixes in numbers based on user-provided parameters, mixing and key, to produce a unique encrypted message. It also supports decoding to retrieve the original text.

## Getting Started
When you start the program, you will see a welcome message with instructions. You can choose to either encrypt (`code`) or decrypt (`decode`) a message.

## Commands
1. code - Use this command to encrypt a message.
2. decode - Use this command to decrypt a previously encrypted message.

## Encryption Process
1. Enter Text: Input the text you want to encrypt.
2. Enter Mixing: Input a number between 1 and 9. This number will be added to the ASCII value of each character.
3. Enter Key: Input another number between 1 and 9. This number will be appended to the end of the ASCII value of each character.

Example:
>>> code
Enter Text: Hello world
Enter Mixing (min - 1, max - 9): 2
Enter Key (min - 1, max - 9): 5

The program will display and save the encrypted text along with the parameters used.

## Decryption Process
1. Enter Text: Input the encrypted text. The program will automatically extract the mixing and key parameters from the text to decrypt it.

Example:

>>> decode
Enter Text: [your encrypted text here]

## Detailed Description of Functions

- file_write(text): Saves the text to coded.txt file.
- coding(text, mixing, key): Encrypts the text using the provided mixing and key parameters.
- decoder_main(text, mixing, key): Decrypts the text using the provided mixing and key parameters.
- search_mix_and_key(text): Extracts the mixing and key parameters from the encrypted text for decryption.

## Note
Ensure the mixing and key parameters are within the specified range (1-9) for proper functioning of the encryption and decryption process.

Start encrypting and decrypting your messages securely with AHC - ASCII Hyper Coder!
