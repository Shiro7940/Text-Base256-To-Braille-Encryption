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
    
def mm(start,num):
    """
    make_map(0x2800,0x2840)
    >>>Output string copied to clipboard
    (⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿)
    (Copied to clipboard, paste it into a txt file and use utf-8 encoding.)
    """
    i= start
    string=""
    while i < start+num:
        string+=chr(i)
        i+=1    
    pyperclip.copy(string)
    print("Output string copied to clipboard")