# create variable for number
number = int(input("enter a number between 1 to 100: "))

# make loop  for number+ add joke

if number <= 25 and number>=0:
    print("Did you hear about the mathematician who’s afraid of negative numbers? ")
    print("He’ll stop at nothing to avoid them.")
elif number <= 50 and number>=26:
    print("Did you hear about the actor who fell through the floorboards?")
    print("He was just going through a stage.")
elif number <= 100 and number>=51:
    print("Did you hear about the claustrophobic astronaut?")
    print("He just needed a little space.")
else:
    print("invalid input")