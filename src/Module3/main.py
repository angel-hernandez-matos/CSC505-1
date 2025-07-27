# File: main.py
# Written by: Angel Hernandez
# Description: Assignment for Critical Thinking - Module 3
# Requirement(s):
#
# You have been contacted and are thinking about developing a "first" prototype for a mobile app that
# let users save a shopping list on their devices. How would you create a preliminary architectural design for it?
# Chose the necessary tools (UML or other diagramming tools) to show your strategy. Then create a series of sketches
# representing the key screens for a paper prototype for the shopping list app. Use Python to write a script that will print out
# the names and number of pages in your prototype and the sequence or flow of the pages.

import os

class MobileAppPage:
    def __init__(self, name):
        self.name = name

class MobileApp:
    mobile_pages = []

    @property
    def pages(self):
        return self.mobile_pages

    def __init__(self, name):
        self.name = name
        self.mobile_pages = [MobileAppPage("Splash Screen"), MobileAppPage("Home Screen"), MobileAppPage("Add New Item"),
                      MobileAppPage("List Items"), MobileAppPage("Settings/About")]

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 3 ***\n')
    app = MobileApp("My Shopping List v.1.0")
    print(f"My Shopping List Mobile App Prototype - Total Pages: {len(app.pages)}")
    print("Page sequence flow as follows: ")
    for x, screen in enumerate(app.pages, start=1):
        print(f"{x}. {screen.name}")

if __name__ ==  '__main__': main()