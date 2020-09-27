import sys
import re

html = "".join(sys.stdin.readlines())

html = re.sub("[\s\n\t]+"," ", html).split(" ")

printStr = ""

for word in html:
    if word == "<br>":
        print(printStr)
        printStr = ""
    
    elif word == "<hr>":
        if printStr:
            print(printStr)
        print("-"*80)
        printStr = ""
    
    else:
        if len(printStr) + len(word) <= 80:
            printStr += ((" " + word) if printStr else word)
        
        else:
            print(printStr)
            printStr = word
            
if printStr:            
    print(printStr)
