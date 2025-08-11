# File: mainDiscussionForum.py
# Written by: Angel Hernandez
# Description: Code snippet for discussion forum - Module 6
# Requirement(s):
#
# The code snippet below demonstrates a simple Python program that creates constructions (their type is
# given by an enum) using a factory. The methods are async to mimic a real-life scenario (It will return once
# it is completed). There is a helper class called "MaintenanceRunner" responsible for performing
# maintenance tasks on the construction.

import os
import asyncio
import random
from enum import Enum, auto
from dataclasses import dataclass

class ConstructionType(Enum):
    BUILDING = auto()
    HOUSE = auto()
    TOWNHOUSE = auto()

class ConstructionColor(Enum):
    WHITE = auto()
    BLUE = auto()
    YELLOW = auto()
    RED = auto()

@dataclass
class Construction:
    rooms: int
    has_garage: bool
    has_garden: bool
    type: ConstructionType
    color: ConstructionColor

class ConstructionFactory:
    @staticmethod
    async def create_construction(type: ConstructionType) -> Construction:
        await asyncio.sleep(random.uniform(0.5, 1.5))  # Simulate async delay
        rooms = random.randint(1, 10)
        has_garage = random.choice([True, False])
        has_garden = random.choice([True, False])
        color = random.choice([ConstructionColor.WHITE, ConstructionColor.BLUE,
                               ConstructionColor.YELLOW, ConstructionColor.RED])
        print(f"Created {type.name} with {rooms} rooms, "
              f"Garage: {has_garage}, Garden: {has_garden} - The Color is {color.name}")

        return Construction(rooms, has_garage, has_garden, type, color)

class MaintenanceRunner:
    def __init__(self, construction: Construction):
        self.construction = construction

    def clean(self):
        print(f"Cleaning the {self.construction.type.name}... Done.")

    def paint(self):
        print(f"Painting the {self.construction.type.name}... Done.")

    def pest_control(self):
        print(f"Performing pest control in the {self.construction.type.name}... Done.")

    def run_all(self):
        self.clean()
        self.paint()
        self.pest_control()

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

async def main():
    clear_screen()
    print('*** Module 6 - Discussion Forum ***\n')
    factory = ConstructionFactory()
    tasks = [
        factory.create_construction(ConstructionType.HOUSE),
        factory.create_construction(ConstructionType.BUILDING),
        factory.create_construction(ConstructionType.TOWNHOUSE)
    ]
    constructions = await asyncio.gather(*tasks)

    for c in constructions:
        runner = MaintenanceRunner(c)
        runner.run_all()

if __name__ ==  '__main__': asyncio.run(main())