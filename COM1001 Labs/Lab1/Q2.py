total=int(input("Enter your shopping amount (TL): "))

if total < 0:
    print("Total amount must be a positive value.")
else:
    print(f"Total Amount: {total} TL")
    if 100 <= total < 500:
        print("Discount Rate: 10%")
        print(f"Payable Amount: {total*.9} TL")
    elif 500 <= total < 1000:
        print("Discount Rate: 20%")
        print(f"Payable Amount: {total*.8} TL")
    elif 1000 <= total:
        print("Discount Rate: 10%")
        print(f"Payable Amount: {total*.7} TL")
    else:
        print("No Discount")

