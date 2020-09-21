


items = ["Banana Bread","Peanut Slush","Papaya Cake"]
prices = [3.5,2.75,4.5]
purchasing = bool(True)
total = 0.0
cart = []
cartq = []
while(purchasing):
    i = 1
    for item in items:
        print(i,") ",item)
        i+= 1
    item_no = int(input("What do you want to buy?"))
    if item_no >3:
        continue
    quantity = int(input("How much do you desire?"))
    cart.append(items[item_no - 1])
    cartq.append(quantity)
    total+= prices[item_no - 1] * quantity

    ans = input("Any more purchases?(y/n)")
    if(ans=="n"):
        purchasing = bool(False)
for x in range(len(cart)):
    print(cart[x],"    ",cartq[x])
print("Total   $",total)

    