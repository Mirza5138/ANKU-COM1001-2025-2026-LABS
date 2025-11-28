#Credits to Muhammet Ali Uludağ for submitting the solution to the repository.

import random
try:
  itemnumber=int(input("Enter the number of items you wanna add"))
  if itemnumber<2:
    print("Enter a valid number")
  else:
    itemlist=[]
    for i in range(itemnumber-1): #Creates a randomly generated knapsack. 
      weight=random.randint(1,20)
      value=random.randint(10,100)
      itemlist.append((weight,value))
    try:
      weight=int(input("Enter a weight"))
      value=int(input("Enter a value"))
      if not(1<=weight<=20) or not(10<=value<=100):
        print("Enter a valid number")
      else:
        itemlist.append((weight,value))
        unsortedver=list(itemlist)
        knapsack=random.randint(20,60)
        for j in range(itemnumber):
          for i in range(itemnumber-1): #Sorts the items to put the most valuable (smaller weight to value ratio) items.
            if itemlist[i+1][1]/itemlist[i+1][0]>itemlist[i][1]/itemlist[i][0]:
              temp=itemlist[i]
              itemlist[i]=itemlist[i+1]
              itemlist[i+1]=temp
        totalweight=0
        totalvalue=0
        result=[]
        for i in itemlist: #Fills the knapsack until it hits the weight limit.
          if totalweight+i[0]<=knapsack:
            result.append(i)
            totalweight+=i[0]
            totalvalue+=i[1]
        print(f"How many items? {itemnumber}\nWeight {weight}\nValue {value}\nAll items: {unsortedver}\nKnapsack capacity {knapsack}\nSorted list: {itemlist}\nSelected items: {result}\nTotal weight {totalweight}\nTotal value: {totalvalue}")
    except:
      print("Enter a valid number")
except:
  print("Enter a valid number")