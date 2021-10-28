def bike_cost(a):
    while a > 1000:
        pricedrop = a*0.1
        a -= pricedrop
        if a > 1000:
            print(a)

cost = int(input("enter your bike cost: "))
bike_cost(cost)

