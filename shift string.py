import pyperclip

def shift_enc(key:int):
    text=input("Please input text to encode: ")
    enc=""
    for char in text:
        char=chr((ord(char)+key))
        enc+=char
    return enc

        
def shift_dec(key:int):
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
        enc=shift_enc(key)
        print(enc)
        pyperclip.copy(enc)
        print("Output string copied to clipboard")        
        dec=shift_dec(key)
        print(dec)
        pyperclip.copy(dec)
        print("Output string copied to clipboard")        
    except Exception as error:
        print("Error: " + str(error))    
    exit = input("Press enter to continue, input to exit: ")
