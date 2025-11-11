def check_password_strength(password):
    lenCheck=False
    capCheck=False
    lowCheck=False
    numCheck=False
    for i in password:
        if not numCheck and "1" <= i <= "9":
            numCheck=True
        if not lowCheck and "a" <= i <= "z":
            lowCheck=True
        if not capCheck and "A" <= i <= "Z":
            capCheck=True
        if not lenCheck and len(password)>=8:
            lenCheck=True
    return lenCheck and lowCheck and capCheck and numCheck

password=input("Enter a password: ")

if check_password_strength(password):
    print("Password is strong")
else:
    print("Password is weak")