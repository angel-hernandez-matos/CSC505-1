# File: main.py
# Written by: Angel Hernandez
# Description: Assignment for Critical Thinking - Module 4
# Requirement(s):
#
# Using your personal experience and observation of people who are excellent software developers, use a UML diagram
# of your choice to depict three personality traits that appear to be common among them. Write a Python Script that
# will print  a brief description and names and number of the important steps in your program.

import os

class DeveloperTrait:
    def describe(self):
        raise NotImplementedError("Subclasses must implement describe().")

class CollaborationTrait(DeveloperTrait):
    def describe(self):
        return "Collaboration: Excels in team communication and shared problem-solving."

class CuriosityTrait(DeveloperTrait):
    def describe(self):
        return "Curiosity: Always eager to explore new technologies and ask 'why'. Challenges status-quo."

class ResilienceTrait(DeveloperTrait):
    def describe(self):
        return "Resilience: Thrives under pressure and never gives up during debugging."

class DeveloperTraitFactory:
    @staticmethod
    def create_trait(trait_name):
        traits_available = {
            "collaboration": CollaborationTrait,
            "curiosity": CuriosityTrait,
            "resilience": ResilienceTrait
        }
        trait_class = traits_available.get(trait_name.lower())
        if trait_class:
            return trait_class()
        else:
            raise ValueError(f"Trait not available: {trait_name}")

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 4 ***\n')
    available_traits = ["collaboration", "curiosity", "resilience"]

    # Steps of the program
    steps = [
        "Define base DeveloperTrait interface.",
        "Implement concrete trait classes.",
        "Create DeveloperTraitFactory.",
        "Use factory to instantiate traits.",
        "Print trait descriptions."
    ]

    print("The steps in DeveloperTraitFactory program are: ")
    for i, step in enumerate(steps, start=1):
        print(f"Step {i}: {step}")

    print("\nThe traits available are: ")

    for trait_name in available_traits:
        trait = DeveloperTraitFactory.create_trait(trait_name)
        print(f"- {trait.describe()}")

if __name__ ==  '__main__': main()