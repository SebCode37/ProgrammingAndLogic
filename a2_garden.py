import random

STARTERS = ["Parsley", "Sage", "Rosemary", "Thyme"]
MAX_RAINFALL = 100

def main():
    """Main function to start the program and display menu"""
    # Print starter instructions
    print("Welcome to the Market Garden Simulator")
    print("Plants cost and generate food according to their name length (e.g., Sage plants cost 4).")
    print("You can buy new plants with the food your garden generates.")
    print(f"You get up to {MAX_RAINFALL} mm of rain per day. Not all plants can survive with less than 30.")
    print("Let's hope it rains... a lot!")
    print("You start with these plants:")

    plants = STARTERS.copy()
    display_plants(plants)
    # Initialize days and food variables
    days = 0
    food = 0
    # Start infinite loop (will end when the user types 'q')
    while True:
        # Print menu
        print(f"After {days} days, you have {len(plants)} plants and your total food is {food}.")
        print("(W)ait")
        print("(D)isplay plants")
        print("(A)dd new plants")
        print("(Q)uit")
        # Get user input
        choice = input("Choose: ").upper()
        # Select given choice
        if choice == "W":
            # If it's W, wait 1 day and increment the days and food counter
            food += wait(plants)
            days += 1
        
        elif choice == "D":
            display_plants(plants)

        elif choice == "A":
            # Get new plant as input, add it to the plants list, decrement the spent food from the food counter
            new_plant = add_plant(plants, food)
            plants.append(new_plant)
            food -= len(new_plant)

        elif choice == "Q":
            # Exit the infinite loop
            break

        else:
            print("Invalid choice!")

    print(f"After {days} days, you have {len(plants)} plants and your total food is {food}.")

    if not plants:
        print("You finished with no plants.")

    print("Thank you for simulating. Now go and enjoy a real garden.")

    
def display_plants(plants):
    """Function to display plants, given the plants list as argument"""
    print(", ".join(plants))


def add_plant(plants, food):
    """Function to get a plant name input from the user. Check if the plant is affordable and valid, given the plants list and food."""
    plant = input("Enter plant name: ").title()
    # Loop until the entered plant is already in the user plants
    while plant in plants:
        print("You already have a", plant, "plant.")
        plant = input("Enter plant name: ").title()

    # If the food is not enough, display error message and return
    if food < len(plant):
        return print(f"With only {food} food, you can't afford {plant}. It costs {len(plant)} food.")

    # Return the selected plant
    return plant
    

def wait(plants):
    """Function to simulate one passing day. Generates food or randomly kills a plant based on the rainfall. Returns the total food produced."""
    # Generate random rainfall number
    rainfall = random.randint(0, MAX_RAINFALL)
    print(f"Rainfall: {rainfall}mm")
    # If the rainfall is < 30 and there is at least one plant
    if rainfall < 30 and plants:
        # Randomly pick a plant from the list and remove it
        died = random.choice(plants)
        plants.remove(died)
        print(f"Sadly, your {died} plant has died.")
        # Set the day's food list to be all 0s
        foods = [0] * len(plants)

    else:
        # Otherwise, set the day's food list to be random numbers between 0 and the plant's name length for every plant
        foods = [random.randint(0, len(plant)) for plant in plants]

    # Print the plant and food produced for all the plants
    for plant, food in zip(plants, foods):
        print(f"{plant} produced {food},", end=" ")
    print()
    # Return the total food
    return sum(foods)


main()


# pseudocode

# func main():
#     print_menu()

#     starter_plants <- STARTERS
#     print_plants(starter_plants)

#     days <- 0
#     food <- 0

#     while user doesn't type q:
#         print_information_menu()
#         choice <- get_user_choice()

#         switch choice:
#             case "W":
#                 wait_day()
#                 days <- days + 1

#             case "D":
#                 print_plants()

#             case "A":
#                 add_plant()

#             default:
#                 print_error_message()