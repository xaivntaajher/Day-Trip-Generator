import random

destinations = ['Los Angeles', 'Las Vegas', 'New York', 'Chicago', 'Orlando']
resturants = ['Olive Garden', 'Red Lobster', 'Hot N Juicy', 'Five Guys', 'Wingstop']
transportations = ['Car', 'Train', 'Airplane', 'Bus', 'Bike']
entertainments = ['Movie', 'Comedy Show', 'Skydiving', 'Bungee Jumping', 'Concert']

def display_destination(list_destinations):
    for place in list_destinations:
        print(place)

def display_resturant(list_resturants):
    for rest in list_resturants:
        print(rest)

def display_transportation(list_transportations):
    for travel in list_transportations:
        print(travel)

def display_entertainment(list_entertainments):
    for ent in list_entertainments:
        print(ent)


random_destination = random.choice(destinations)
print(f'Destination: {random_destination}')
random_resturant = random.choice(resturants)
print(f'Resturant: {random_resturant}')
random_transportation = random.choice(transportations)
print(f'Transportation: {random_transportation}')
random_entertainment = random.choice(entertainments)
print(f'entertainment: {random_entertainment}')

satisfy = input('Are you satisfy with your trip? ')
print(satisfy)

yes = 'y'
if yes == 'y':
    print(f'Destination: {random_destination}')
    print(f'Resturant: {random_resturant}')
    print(f'Transportation: {random_transportation}')
    print(f'entertainment: {random_entertainment}')

no = 'n'
if no == 'n':
    




# (5 points): As a developer, I want to make at least three commits with descriptive messages -
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. -
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of 
#              entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10  points): As a user, I want to display my completed trip in the console
# (5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 