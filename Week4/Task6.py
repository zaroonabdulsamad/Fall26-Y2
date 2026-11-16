total_revenue=0

while True:
    unit=int(input("Enter the UNI consumed:"))
    if unit==-1:
        break
    elif unit<0:
        print("Invalid units!")
    elif unit<=100:
        bill=unit*10
    elif unit<=200:
        bill=(100*10)+(unit-100)*15
    elif unit<300:
        bill=(100*10)+(100*15)+(unit-200)*25
    else:
        bill=(100*10)+(100*15)+(100*20)+(unit-300)*25

    print("Customer Bill is: Rs.",bill)
    total_revenue+=bill
print("Total Revenue: Rs.", total_revenue)