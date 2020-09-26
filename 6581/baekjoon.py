import sys

inputText = sys.stdin.readlines()

# remove enter and split
formedTextList = []

for line in inputText:
    if line.strip().replace("\n", "").split():
        formedTextList += line.strip().replace("\n", "").split()
        

printStr = ""

for data in formedTextList:
    if data == "<br>":
        print(printStr)
        printStr = ""
    
    elif data == "<hr>":
        if(printStr):
            print(printStr)
        print("-"*80)
        printStr = ""
        
    else:
        if len(printStr) + len(data) <= 80:
            if len(printStr):
                printStr += " " + data
            else:
                printStr = data
        else:
            print(printStr)
            printStr = data
            
if printStr:         
    print(printStr)
