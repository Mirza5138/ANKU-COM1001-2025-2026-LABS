# I know I didn't define a function as the assignment suggested but you can implement it as an exercise. xd

transactions = open("Q2 input.txt","r")

stock = {}

for i in transactions: #Reads each line.
    request = i.rstrip().split(":") #Splits the request into 3 segments.
    if request[0] == "receive": 
        stock[request[1]] = stock.get(request[1],0) + int(request[2])
        print(f"Received: {request[2]} x '{request[1]}'. New stock: {stock[request[1]]}")
    elif request[0] == "sell":
        if stock.get(request[1],0)>=int(request[2]): #Checks wheter there is enough stock or not.
            stock[request[1]] = stock.get(request[1],0) - int(request[2])
            print(f"Sold: {request[2]} x '{request[1]}'. Remaining stock: {stock[request[1]]}")
        else:
            print(f"SALE FAILED: Tried to sell {request[2]} x '{request[1]}', but only {stock[request[1]]} in stock.")
    else:
        print(f"Skipping malformed line: '{request[0]}'")

print(f"Final Inventory Report: {stock}")