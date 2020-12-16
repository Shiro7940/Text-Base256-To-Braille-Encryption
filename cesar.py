import pyperclip

def cesar_enc(key:int):
    text=input("Please input text to encode: ")
    enc=""
    for char in text:
        char=chr((ord(char)+key))
        enc+=char
    return enc

        
def cesar_dec(key:int):
    text=input("Please input text to decode: ")
    dec=""
    for char in text:
        char=chr((ord(char)-key))
        dec+=char
    return dec

exit = ""    
while exit == "":
    try:
        key= int(input("Please input key: "))
        enc=cesar_enc(key)
        print(enc)
        pyperclip.copy(enc)
        print("Output string copied to clipboard")        
        dec=cesar_dec(key)
        print(dec)
        pyperclip.copy(dec)
        print("Output string copied to clipboard")        
    except Exception as error:
        print("Error: " + str(error))    
    exit = input("Press enter to continue, input to exit: ")