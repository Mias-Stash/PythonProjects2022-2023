#ceasar cypher
#11/28/2023
#encrypt
def encryptstr(message):
    #declare
    newstring = str()
    AsciiLetterValue = int()
    OneLetter = str()
    NewAsciiValue = int()
    #loop to assign new ascii value
    for index in range(0, len(message)):
        OneLetter = message[index]
        AsciiLetterValue = ord(OneLetter)
        #checking for z or Z
        if AsciiLetterValue == 122:
            NewAsciiValue = 97
        elif AsciiLetterValue == 90:
            NewAsciiValue = 65
        #assign new ascii value if not z or Z
        else:
            NewAsciiValue = AsciiLetterValue + 1
        #create the new string
        newstring = newstring + chr(NewAsciiValue)
    return newstring
#decrypt
def decryptstr(message):
        #declare
    newstring = str()
    AsciiLetterValue = int()
    OneLetter = str()
    NewAsciiValue = int()
    #loop to assign new ascii value
    for index in range(0, len(message)):
        OneLetter = message[index]
        AsciiLetterValue = ord(OneLetter)
        #checking for z or Z
        if AsciiLetterValue == 97:
            NewAsciiValue = 122
        elif AsciiLetterValue == 65:
            NewAsciiValue = 90
        #assign new ascii value if not z or Z
        else:
            NewAsciiValue = AsciiLetterValue - 1
        #create the new string
        newstring = newstring + chr(NewAsciiValue)
    return newstring
#main
def main():
    #declare
    text = str()
    choice = str()
    #input
    text = input("Enter text: ")
    choice = input("(E)ncrypt or (D)ecrypt? ")
    #elif stuff
    if choice == "E":
        print(encryptstr(text))
    elif choice == "D":
        print(decryptstr(text))
    else:
        print("Invalid choice.")
main()
    
