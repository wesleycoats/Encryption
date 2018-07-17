#!/bin/python3
#author Wesley Coats

#character lists for encryption/decryption
alphabet = 'abcdefghijklmnopqrstuvwxyz'
upperAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numberLine = '0123456789'

#Returns a valid key between 1-26 as a number
def keyCheck(key, choice):
    #Checks is key is a number
    if key.isnumeric():
        key = int(key)
        #Checks if key is between 1-26
        if key > 0 and key < 27:
            return int(key)
        #Reprompts for valid key if key is out of range
        else:
            print("Please enter a valid key from 1-26.")
            if(choice == "e"):
                newKey = input("Please enter a key for encryption (1-26): ")
                return keyCheck(newKey, "e")
            elif(choice == "d"):
                newKey = input("Please enter the key to be used for decryption (1-26): ")
                return keyCheck(newKey, "d")
    #Reprompts if key is not a number
    else:
        print("Please enter a valid key from 1-26.")
        if(choice == "e"):
            newKey = input("Please enter a key for encryption (1-26): ")
        elif(choice == "d"):
            newKey = input("Please enter the key to be used for decryption (1-26): ")
            return keyCheck(newKey, "d")
    
#Asks user if they want to encrypt or decrypt a message
def promptUser():
    choice = ("Do you want to (e)ncrypt or (d)ecrypt a message?")
    while choice != 'e' and choice != 'd':
        print("Please enter \"e\" for encrypt or \"d\" for decrypt.")
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message?")

    if choice == 'e':
        encrypt()
    elif choice == 'd':
        decrypt()

#Uses Caesar cipher to translate messages character by character
def charByChar(message, key):
    newMessage = ''
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + int(key)) % 26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        elif character in upperAlphabet:
            position = upperAlphabet.find(character)
            newPosition = (position + int(key)) % 26
            newCharacter = upperAlphabet[newPosition]
            newMessage += newCharacter
        elif character in numberLine:
            position = numberLine.find(character)
            newPosition = (position + int(key)) % 10
            newCharacter = numberLine[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    
        print("The new message is: ", newMessage)
    print("The final message is: ", newMessage)  

#Encrypts a message
def encrypt():
    key = input("Please enter a key for encryption (1-26): ")
    key = keyCheck(key, "e")
    message = input("Please enter a message to be encrypted: ")
    charByChar(message, key)
  
#Decrypts a message  
def decrypt():
    key = input("Please enter the key to be used for decryption (1-26): ")
    key = keyCheck(key, "d")
    key = 26 - key
    message = input("Please enter the encrypted message: ")
    charByChar(message, key)

#Prompts user if they want to encrypt or decrypt another message or quit
def reprompt():
    again = input("(d)ecrypt a message or (e)ncrypt another message or (q)uit?")
    while again != 'd' and again != 'e' and again != 'q':
        print("Please enter \"d\" for decrypt or \"e\" for encrypt or \"q\" for quit.")
        again = input("(d)ecrypt a message or (e)ncrypt another message or (q)uit?")
    if again == 'e':
        encrypt()
        reprompt()
    elif again == 'd':
        decrypt()
        reprompt()
    elif again == 'q':  
        exit()


promptUser()
reprompt()