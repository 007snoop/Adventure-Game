# Fuctions and data structures for dungeons
import time

def talk_to_npc():
    print("\nYou approach the mysterious NPC...")
    time.sleep(1)
    while True:
        # Display NPC options
        print("\nWhat will you do?")
        print("1. Talk to the NPC.")
        print("2. ### Options.\n")
    
        choice = input("Enter your choice: ")

        if choice == "1":
            time.sleep(1)
            print("\nThe NPC gives you a quest!")
            time.sleep(1)
        elif choice == "2": 
            time.sleep(1)
            print("The NPC is an option.")
            time.sleep(1)
        else:
            time.sleep(1)
            print("Leaving the NPC.")
            break
        
            
    
def explore_dungeon():
    print("\nYou enter the dark dungeon...")
    # Add more narrative and choices here
    print("You encounter a monster!")
