num=int(input("Enter a number: "))
cloneNum=num
palindrome=0

while cloneNum>0:
    palindrome=palindrome*10+cloneNum%10
    cloneNum//=10

if palindrome==num:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")