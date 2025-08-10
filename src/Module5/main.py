# File: main.py
# Written by: Angel Hernandez
# Description: Assignment for Critical Thinking - Module 5
# Requirement(s):
#
# The department of public works for a large city has decided to develop a web-based pothole tracking and repair
# system (PHTRS). A description follows:
#
#  Citizens can log onto a website and report the location and severity of potholes. As potholes are reported,
#  they are logged within a "public works department repair system" and are assigned an identifying number,
#  stored by street address, size (on a scale of 1 to 10), location (middle, curb, etc.), district
#  (determined from street address), and repair priority (determined from the size of the pothole).
#
# Work order data are associated with each pothole and include pothole location and size, repair crew identifying
# number, number of people on crew, equipment assigned, hours applied to repair, hole status (work in progress,
# repaired, temporary repair, not repaired), amount of filler material used, and cost of repair (computed from
# hours applied, number of people, material and equipment used).
#
# Finally, a damage file is created to hold information about reported damage due to the pothole and includes
# the citizen's name, address, phone number, type of damage, and dollar amount of damage. PHTRS is an online system;
# all queries are to be made interactively.
#
# Draw a UML use case diagram for a PHTRS system. You'll have to make a number of assumptions about the manner
# in which a user interacts with this system. Use Python to write a script that will print out the different actors
# and use cases  and a brief description of your diagram.

import os

class ActorsUseCasesDescriptions:
    @staticmethod
    def print():
        # Actors, use cases and diagram description
        actors = {
            "Citizen:": " Submits pothole details and checks repair status.",
            "PHTRS System:": " Processes reports, generates work orders, and manages repair data and work orders.",
            "Repair Crew:": " Executes assigned work orders and updates repair status."
        }

        use_cases = {
            "Report Pothole:": " Citizen logs onto the website and submits pothole details.",
            "Log details in PHTRS:": " Information about pothole is logged in PHTRS.",
            "Generate Work Order:": " PHTRS System creates a work order based on reported pothole.",
            "Assign Repair Crew:": " System assigns a crew to handle the repair.",
            "Update Repair Status:": " Repair Crew updates the system with progress and completion info."
        }

        diagram_description = {
            "Firstly,": "the sequence diagram shows the flow of messages between objects (actors) and how they interact.",
            "Then,": "the class diagram shows the static structure of the system by illustrating its classes "+
                         "with their attributes and operations, and they're related.",
            "Lastly,": "the use case diagram shows the actors and their use cases."
        }

        print_info = {
            "*** ACTORS ***": actors,
            "*** USE CASES ***": use_cases,
            "*** DIAGRAM DESCRIPTION ***": diagram_description
        }

        for stage, details in print_info.items():
            print(f"\n{stage}\n")
            for key, value in details.items():
                print(f"\t{key}{value}")
        print()

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 5 - Critical Thinking ***\n')
    ActorsUseCasesDescriptions.print()

if __name__ ==  '__main__': main()