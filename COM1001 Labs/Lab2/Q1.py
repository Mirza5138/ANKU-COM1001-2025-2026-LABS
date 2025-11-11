num=int(input("Enter a number: "))
divSum=0
i=1

#Go through the numbers until the number itself and add them to divSum if it is a divisor.
while i<num:
    if num%i==0:
        divSum+=i
    i+=1

if divSum==num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
