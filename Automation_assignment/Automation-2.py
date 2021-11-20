import re

def regex_strip(str, ptrn=None):
    if not ptrn:
        strip_front = re.compile(r'^\s*') 
        strip_back = re.compile(r'\s*$') 

        str = re.sub(strip_front, "", str)
        str = re.sub(strip_back, "", str) 

    else:
        strip_char = re.compile(ptrn)
        str = re.sub(strip_char, "", str)
    return str

string = input("Enter string to be stripped: ")
ptrn = input("Enter character to be removed, if none press enter: ")
print(regex_strip(string, ptrn))        