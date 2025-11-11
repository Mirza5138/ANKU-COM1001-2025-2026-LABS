strg=input("Input: ")
letterStack=[] #Creates a list to store letters of individual words.
newString=""

for i in strg:
    if i==" ": #Adds the letters in the stack to the result string and empties the letter stack if it stumbles upon a space character.
        for j in letterStack:
            newString+=j
        newString+=" "
        letterStack=[]
    else: #Inserts the leter at the start of the stack.
        letterStack.insert(0,i)
for j in letterStack:
    newString+=j

print(f"Output: {newString}")
