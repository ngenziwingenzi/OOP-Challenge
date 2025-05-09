class Pet:
    def __init__(self, name):
        """Initialize a pet with the given name and default attributes."""
        print(f"Creating pet: {name}")
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5 
        self.tricks = []
    
    def eat(self):
        """Feed the pet to reduce hunger and slightly increase happiness."""
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
    
    def sleep(self):
        """Let the pet sleep to restore energy."""
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5) 
    
    def play(self):
        """Play with the pet to increase happiness but consume energy and increase hunger."""
        print(f"{self.name} is playing...")
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
    
    def get_status(self):
        """Display the current status of the pet."""
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}")
    
    def train(self, trick):
        """Teach the pet a new trick."""
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 1)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned: {trick}")
        else:
            print(f"{self.name} already knows how to {trick}")
    
    def show_tricks(self):
        """Display all tricks the pet has learned."""
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
