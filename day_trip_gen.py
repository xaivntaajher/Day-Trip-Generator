import random

destinations = ['Los Angeles', 'Las Vegas', 'New York', 'Chicago', 'Orlando']
resturants = ['Olive Garden', 'Red Lobster', 'Hot N Juicy', 'Five Guys', 'Wingstop']
transportations = ['Car', 'Train', 'Airplane', 'Bus', 'Bike']
entertainments = ['Movie', 'Comedy Show', 'Skydiving', 'Bungee Jumping', 'Concert']

def display_destination(list_destinations, list_resturants, list_transportations, list_entertainments):
    for place in list_destinations:
        print(place)
    for rest in list_resturants:
        print(rest)
    for travel in list_transportations:
        print(travel)
    for ent in list_entertainments:
        print(ent)

# def display_destination(list_destinations): 
#     for place in list_destinations:
#         print(place)

# def display_resturant(list_resturants):
#     for rest in list_resturants:
#         print(rest)

# def display_transportation(list_transportations):
#     for travel in list_transportations:
#         print(travel)

# def display_entertainment(list_entertainments):
#     for ent in list_entertainments:
#         print(ent)

def display_new_destination(list_new_destinations, list_new_resturants, list_new_transportations, list_new_entertainments):
    for new_place in list_new_destinations:
        print(new_place)
    for new_rest in list_new_resturants:
        print(new_rest)
    for new_travel in list_new_transportations:
        print(new_travel)
    for new_ent in list_new_entertainments:
        print(new_ent)   

# def display_new_destination(list_new_destinations):
#     for new_place in list_new_destinations:
#         print(new_place)

# def display_new_resturant(list_new_resturants):
#     for new_rest in list_new_resturants:
#         print(new_rest)

# def display_new_transportation(list_new_transportations):
#     for new_travel in list_new_transportations:
#         print(new_travel)

# def display_new_entertainment(list_new_entertainments):
#     for new_ent in list_new_entertainments:
#         print(new_ent)

random_new_destination = random.choice(destinations)
random_new_resturant = random.choice(resturants)
random_new_transportation = random.choice(transportations)
random_new_entertainment = random.choice(entertainments)


random_destination = random.choice(destinations)
print(f'Destination: {random_destination}')
random_resturant = random.choice(resturants)
print(f'Resturant: {random_resturant}')
random_transportation = random.choice(transportations)
print(f'Transportation: {random_transportation}')
random_entertainment = random.choice(entertainments)
print(f'Eyntertainment: {random_entertainment}')

satisfy = input('Are you satisfied with your trip? Y or N ')
print(satisfy)

if satisfy == 'Y':
    print(f'Have fun and enjoy your trip!')
    print(f'Destination: {random_destination}')
    print(f'Resturant: {random_resturant}')
    print(f'Transportation: {random_transportation}')
    print(f'Entertainment: {random_entertainment}')
elif satisfy == 'N':
    not_satify = input('What would you like to change? Destination, Resturant, Transportation, Entertainment ' )
    if not_satify == 'Destination':
        print(f'Destination: {random_new_destination}')
        print(f'Resturant: {random_resturant}')
        print(f'Transportation: {random_transportation}')
        print(f'Entertainment: {random_entertainment}')
    elif not_satify == 'Resturant':
        print(f'Destination: {random_destination}')
        print(f'Resturant: {random_new_resturant}')
        print(f'Transportation: {random_transportation}')
        print(f'Entertainment: {random_entertainment}')
    elif not_satify == 'Transportation':
        print(f'Destination: {random_destination}')
        print(f'Resturant: {random_resturant}')
        print(f'Transportation: {random_new_transportation}')
        print(f'Entertainment: {random_entertainment}')
    elif not_satify == 'Entertainment':
        print(f'Destination: {random_destination}')
        print(f'Resturant: {random_resturant}')
        print(f'Transportation: {random_transportation}')
        print(f'Entertainment: {random_new_entertainment}')

    new_satify = input('Are you now satisfied with your trip? Y or N ')
    print(new_satify)
    if new_satify == "Y":
        print()
    elif new_satify == 'N':
        print(not_satify)
        # print(f'Destination: {random_new_destination}')
        # print(f'Resturant: {random_new_resturant}')
        # print(f'Transportation: {random_new_transportation}')
        # print(f'Entertainment: {random_new_entertainment}')    

            
    




    








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