num=int(input("Enter a number: "))
cloneNum=num #Makes a duplicate of the input to do the operations on.
palindrome=0

#Puts the number in reverse using arithmetic.
while cloneNum>0:
    palindrome=palindrome*10+cloneNum%10
    cloneNum//=10

if palindrome==num:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
