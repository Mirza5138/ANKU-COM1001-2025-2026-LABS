num=int(input("Enter a number: "))
divSum=0
i=1

while i<num:
    if num%i==0:
        divSum+=i
    i+=1

if divSum==num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")