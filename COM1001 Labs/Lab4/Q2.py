strg=input("Input: ")
letterStack=[]
newString=""

for i in strg:
    if i==" ":
        for j in letterStack:
            newString+=j
        newString+=" "
        letterStack=[]
    else:
        letterStack.insert(0,i)
for j in letterStack:
    newString+=j

print(f"Output: {newString}")