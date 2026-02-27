# Function that takes name and quest as parameters
def personalized_greeting(name, quest):
    print(f"Greetings, {name}! May your {quest} be successful!")

# Get user's name
name = input("What is your name? ")
# Get user's quest
quest = input("What is your quest? ")
# Call function with user's inputs
personalized_greeting(name, quest) 
