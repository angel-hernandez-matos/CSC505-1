# File: main.py
# Written by: Angel Hernandez
# Description: Assignment for Critical Thinking - Module 2
# Requirement(s):
#
# Implement the YourLastName class using Python, which will prompt the user to input the key elements
# of the diagram and return these objects in a well-formatted output.

import os
import inflect

class RenderElement:
     @staticmethod
     def draw_element(text, width = 30):
         lines = text.split('\n')
         element = ["╔" + "═" * width + "╗"]

         for line in lines:
             element.append("║" + line.center(width) + "║")
         element.append("╚" + "═" * width + "╝")

         return element

     @staticmethod
     def connect_elements(elements):
         retval = []
         for i, element in enumerate(elements):
             retval.extend(element)
             if i < len(elements) - 1:
                 retval.append(" " * (len(element[0]) // 2) + "↓")

         return "\n".join(retval)

class Hernandez:
    @staticmethod
    def produce_output(elements):
        max_length = len(max(elements, key=len))
        objects_to_render = [RenderElement.draw_element(text, max_length) for text in elements]
        print(RenderElement.connect_elements(objects_to_render))

class UiElementFactory:
    name = ""
    elements = None
    key_element_names =[]

    def __init__(self, name):
        self.name = name

    def prompt_user(self):
        count = 0
        number_to = inflect.engine()
        print(f"Welcome to {self.name} Model!")
        print("Please enter your key elements (blank entry exits)\n")

        while True:
            count = count + 1
            key_element = input(f"Enter {number_to.ordinal(count)} element's  name: ")
            if not key_element.strip():
                break
            else:
               self.key_element_names.append(key_element)

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 2 ***\n')
    ui_factory = UiElementFactory("Angel's Model")
    ui_factory.prompt_user()

    if not ui_factory.key_element_names:
        print("You didn't enter any key elements!")
    else:
        Hernandez.produce_output(ui_factory.key_element_names)

if __name__ ==  '__main__': main()