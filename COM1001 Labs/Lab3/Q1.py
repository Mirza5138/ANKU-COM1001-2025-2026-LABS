amount=int(input("Enter a positive integer: "))

for i in range(amount):
    print(" "*(amount-i-1)+"*"*(2*i+1))