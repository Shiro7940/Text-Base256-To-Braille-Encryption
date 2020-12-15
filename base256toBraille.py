import math
import pyperclip

def make_map(start,end):
    """
    make_map(0x2800,0x2840)
    >>>Output string copied to clipboard
    (⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿)
    (Copied to clipboard, paste it into a txt file and use utf-8 encoding.)
    """
    i= start
    string=""
    while i <= end:
        string+=chr(i)
        i+=1    
    pyperclip.copy(string)
    print("Output string copied to clipboard")

def encode(text,encodeMap,encodingBit):
    binary = ''.join([format(x, '08b') for x in text.encode('utf-8')])
    binary += (encodingBit - len(binary) % encodingBit) * '0'
    splittedArray = [binary[x:x + encodingBit] for x in range(0, len(binary), encodingBit)]
    encodedString = ''.join([encodeMap[int(x, 2)] for x in splittedArray])
    encodedString += (2 - len(encodedString) % 2) * '='
    return encodedString

def decode(text,encodeMap,encodingBit):
    text = text.replace('=', '')
    indexMap = [encodeMap.index(x) for x in text]
    binString = ''.join([format(x, f'0{encodingBit}b') for x in indexMap])
    binString += (8 - len(binString) % 8) * '0'
    binArray = [binString[x:x + 8] for x in range(0, len(binString), 8)]
    decodedString = bytes([int(x, 2) for x in binArray]).decode('utf-8')
    decodedString = decodedString.replace('\000', '')
    return decodedString


try:
    map_name = str(input("Please input map name: "))
    if map_name == "64":
        map_name = "base64.map"
    elif map_name == "bagua":
        map_name = "base64bagua.map"
    elif len(map_name) < 2:
        map_name = "base256Braille.map"
    encmap = open(map_name,"r",encoding="utf-8")
    
except:
    map_name = "base256Braille.map"
    encmap = open(map_name,"r",encoding="utf-8")
    #default setting
try:    
    encodeMap = list(encmap.read())
    if len(encodeMap) % 2 != 0:
        encodeMap = encodeMap[(len(encodeMap) % 2):]
    #get rid of excessive characters
except Exception as error:
    print("Error: " + str(error))
    
exit = ""    
while exit == "":
    try:
        print("-----ENCODE-----")
        text = str(input("Please input text to encode: "))
        encodingBit = math.floor(math.log2(len(encodeMap)))
        print('Base' + str(2**encodingBit) + ' (Map Size: ' + str(len(encodeMap)) + ')'+' (Map Name: ' + map_name + ')')        
        enc_result=encode(text,encodeMap,encodingBit)
        if map_name == "base256Braille.map":
            enc_result = enc_result.replace("\u2800","")
            enc_result = enc_result.replace("=","")
        if map_name == "base64bagua.map":
            enc_result = enc_result.replace('=','\u262F')
        print("Result: " + enc_result)
        print("Lenth: " + str(len(enc_result)))
        check_result = enc_result
        for character in check_result:
            if character not in encodeMap:
                check_result = check_result.replace(character,"")
        if decode(check_result,encodeMap,encodingBit) == text:
            print("Verify success")
        else: 
            print("Verify failed")
            
        pyperclip.copy(enc_result)
        print("Output string copied to clipboard")
        
        print("-----DECODE-----")
        text = str(input("Please input text to decode: "))
        for character in text:
            if character not in encodeMap:
                text = text.replace(character,"")
        dec_result = decode(text,encodeMap,encodingBit)
        print(dec_result)
        
        pyperclip.copy(dec_result)
        print("Output string copied to clipboard")     
        
    except Exception as error:
        print("Error: " + str(error))    
    exit = input("Press enter to continue, input to exit: ")