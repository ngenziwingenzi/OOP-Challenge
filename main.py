from pet import Pet

def main():
    max_pet = Pet("Max")
    
    # Test basic functionality
    max_pet.eat()
    max_pet.play()
    max_pet.sleep()
    
    # Train some tricks
    max_pet.train("roll over")
    max_pet.train("play dead")
    
    # Display the pet's current status
    max_pet.get_status()
    
    # Additional tests to demonstrate edge cases
    print("\n--- Additional Tests ---")
    
    # Try teaching the same trick again
    max_pet.train("roll over")
    
    # Multiple actions to see how values change
    print("\nFeeding Max multiple times:")
    max_pet.eat()
    max_pet.eat()
    
    # Show final status
    print("\nFinal status after multiple feedings:")
    max_pet.get_status()

if __name__ == "__main__":
    main()
