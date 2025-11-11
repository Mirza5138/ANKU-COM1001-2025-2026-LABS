#Take inputs
not1=int(input("Enter the 1st exam grade: "))
not2=int(input("Enter the 2nd exam grade: "))
not3=int(input("Enter the 3rd exam grade: "))

#Go through the if conditions to see which grade it falls under.
if 0 <= not1 <= 100 and 0 <= not2 <= 100 and 0 <= not3 <= 100:
    ortalama=(not1+not2+not3)/3
    print(f"Average: {ortalama}")
    print("Letter grade: ",end="")
    if ortalama >= 90:
        print("AA")
        print("Congratulations, you passed!")
    elif ortalama >= 80:
        print("BA")
        print("Congratulations, you passed!")
    elif ortalama >= 70:
        print("BB")
        print("Congratulations, you passed!")
    elif ortalama >= 60:
        print("CB")
        print("Congratulations, you passed!")
    elif ortalama >= 50:
        print("CC")
        print("Congratulations, you passed!")
    elif ortalama >= 40:
        print("DC")
        print("Unfortunately, you failed.")
    elif ortalama >= 30:
        print("DD")
        print("Unfortunately, you failed.")
    else:
        print("FF")
        print("Unfortunately, you failed.")
else:
    print("Invalid grade (should be between 0-100)")
