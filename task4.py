#create variable to enter the cost of the bike
cost = 2000

# Create loop for reducing price and display the results.
while cost > 1000:
    pricedrop = cost * 0.1
    cost -= pricedrop 
    if cost > 1000:
        print(cost)