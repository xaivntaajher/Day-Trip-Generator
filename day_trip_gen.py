import random

destinations = ['Los Angeles', 'Las Vegas', 'New York', 'Chicago', 'Orlando']
resturants = ['Olive Garden', 'Red Lobster', 'Hot N Juicy', 'Five Guys', 'Wingstop']
transportations = ['Car', 'Train', 'Airplane', 'Bus', 'Bike']
entertainments = ['Movie', 'Comedy Show', 'Skydiving', 'Bungee Jumping', 'Concert']



# def display_day_trip(destinations, resturants, transportations, entertainments):
#     random_destination = random.choice(destinations)
#     print(f'Destination: {random_destination}')
#     random_resturant = random.choice(resturants)
#     print(f'Resturant: {random_resturant}')
#     random_transportation = random.choice(transportations)
#     print(f'Transportation: {random_transportation}')
#     random_entertainment = random.choice(entertainments)
#     print(f'Eyntertainment: {random_entertainment}')
#     return (random_destination, random_resturant, random_transportation, random_entertainment)
   


random_destination = random.choice(destinations)
print(f'Destination: {random_destination}')
random_resturant = random.choice(resturants)
print(f'Resturant: {random_resturant}')
random_transportation = random.choice(transportations)
print(f'Transportation: {random_transportation}')
random_entertainment = random.choice(entertainments)
print(f'Eyntertainment: {random_entertainment}')


trip = input('Are you satisfied with your trip? Y or N ')
print(trip)

# def print_day_trip()

if trip == 'Y':
    print('Have fun and enjoy your trip!')
    print(f'Destination: {random_destination}')
    print(f'Resturant: {random_resturant}')
    print(f'Transportation: {random_transportation}')
    print(f'Entertainment: {random_entertainment}')
elif trip == 'N':
    # Destination = random_destination
    # Resturant = random_resturant
    # Transportation = random_transportation
    # Entertainment = random_entertainment
    
    # need def function and use for loop
    user_input = ""
    while user_input != 'Y':
        new_trip = input(f'What would you like to change? Destination, Resturant, Transportation, Entertainment ' )
        if new_trip == 'Destination':
            random_destination = random.choice(destinations)
        elif new_trip == 'Resturant':
            random_resturant = random.choice(resturants)
        elif new_trip == 'Transportation':
            random_transportation = random.choice(transportations)
        elif new_trip == 'Entertainment':
            random_entertainment = random.choice(entertainments)

        print(f'Destination: {random_destination}')
        print(f'Resturant: {random_resturant}')
        print(f'Transportation: {random_transportation}')
        print(f'Entertainment: {random_entertainment}')
        
        # need def function and for loop
        user_input = input('Are you now satisfied with your trip? Y or N ')


              
              

            
    

# def run_day_trip_gen():
# def print_full_trip(list_of_options):
# def generate_random_item(list_of_items):
# def determine_satisfication(current_trip, trip options):
# def re_select_options(current_trip, options):
# run_day_trip_gen()


    
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