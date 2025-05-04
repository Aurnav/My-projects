import random

def pet_menu():
    
    moods = ["Happy", "Sad", "Excited", "Hungry", "Sleepy"]
    pet_mood = random.choice(moods)
    
    
    health = 100
    mood = 50
    
    
    reaction_map = {
        "Hungry": {
            "Feed": 10,
            "Play": -10,
            "Sleep": 0
        },
        "Sleepy": {
            "Feed": 0,
            "Play": -5,
            "Sleep": 10
        },
        "Happy": {
            "Feed": 5,
            "Play": 10,
            "Sleep": 5
        },
        "Sad": {
            "Feed": 5,
            "Play": 0,
            "Sleep": 5
        },
        "Excited": {
            "Feed": 5,
            "Play": 15,
            "Sleep": 0
        }
    }

    while True:
        print("\nYour pet is currently:", pet_mood)
        print(f"Health: {health} | Mood: {mood}")
        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Exit")

        choice = input("Enter your choice: ").lower()

        
        if choice == "1":
            action = "Feed"
        elif choice == "2":
            action = "Play"
        elif choice == "3":
            action = "Sleep"
        elif choice == "4":
            print("Goodbye! Your pet will miss you.")
            break
        else:
            print("Nope, invalid choice.")
            continue

        
        health += reaction_map[pet_mood].get(action, 0)
        mood += 5  

        
        if health <= 0 or mood <= 0:
            print("\nYour pet doesn’t like you anymore. Game over.")
            break

      
        pet_mood = random.choice(moods)

pet_menu()
