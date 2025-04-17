class Pet:
  def __init__(self, name):
        self.name = name
        self.hunger = 5        # setting default mid-level
        self.energy = 5        # setting default mid-level
        self.happiness = 5     # setting default mid-level
        self.tricks = []       # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f" - {trick}")
            else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"Pet Name: {self.name}")
        print(f"Hunger: {self.hunger} of 10")
        print(f"Energy: {self.energy} of 10")
        print(f"Happiness: {self.happiness} of 10")

