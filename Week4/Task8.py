stock=100
total_sales=0

while True:
    quantity_sold=int(input("Enter Quantity Sold: "))

    if quantity_sold == -1:
        break

    elif quantity_sold>stock:
        print("Not enough stock! Transaction Rejected!")
        continue
    elif quantity_sold<=0:
        print("Invalid Quantity! Try Again!")
        continue

    stock-=quantity_sold
    total_sales+=quantity_sold
    print("Remaining Stock:", stock)

    if stock==0:
        break

print("Total Units Sold:", total_sales)
print("Remaining Stock:", stock)



