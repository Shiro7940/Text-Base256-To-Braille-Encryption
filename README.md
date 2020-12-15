# Base256-to-Braille
Convert text to unicode Braille (or any other characters) using modified baseN.py from uetchy
(https://github.com/uetchy/baseN)
* You can disable the auto copy by # all the the code related to pyperclip. 
* You can use the make_map function to generate different maps.
## An example of running the script:
```
[evaluate base256toBraille.py]
Please input map name: base256Braille.map
-----ENCODE-----
Please input text to encode: this is a test
Base256 (Map Size: 256) (Map Name: base256Braille.map)
Result: ⡴⡨⡩⡳⠠⡩⡳⠠⡡⠠⡴⡥⡳⡴
Lenth: 14
Verify success
Output string copied to clipboard
-----DECODE-----
Please input text to decode: ⡴⡨⡩⡳⠠⡩⡳⠠⡡⠠⡴⡥⡳⡴
this is a test
Output string copied to clipboard
Press enter to continue, input to exit: exit

```
