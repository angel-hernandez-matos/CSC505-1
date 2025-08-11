# File: main.py
# Written by: Angel Hernandez
# Description: Module 6 - Critical Thinking
# Requirement(s):
#
# Apply a “stepwise refinement approach” to develop three different levels of procedural abstractions
# for the following program:
#
# Develop a check writer that, given a numeric dollar amount, will print the amount in words normally required on a check.

import os

class CheckWriter:
    __Ones__ = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    __Teens__ = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    __Tens__ = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def __init__(self):
        self.__convert_number_to_words = self.__get_recursive_lambda_for_parsing()

    def __get_recursive_lambda_for_parsing(self):
        def retval(n):
            dispatch = {
                'zero': lambda: self.__Ones__[0],
                'ones': lambda: self.__Ones__[int(n)],
                'teens': lambda: self.__Teens__[int(n) - 10],
                'tens': lambda: self.__Tens__[int(n) // 10] + ("-" + self.__Ones__[int(n) % 10] if n % 10 != 0 else ""),
                'hundreds': lambda: retval(n // 100) + " hundred" + (" and " + retval(n % 100) if n % 100 != 0 else ""),
                'thousands': lambda: retval(n // 1000) + " thousand" + (", " + retval(n % 1000) if n % 1000 != 0 else ""),
                'millions': lambda: retval(n // 1_000_000) + " million" + (
                    ", " + retval(n % 1_000_000) if n % 1_000_000 != 0 else ""),
                'too_large': lambda: "The number is too large. Maximum is 10 million."
            }

            if n == 0:
                return dispatch['zero']()
            elif n < 10:
                return dispatch['ones']()
            elif n < 20:
                return dispatch['teens']()
            elif n < 100:
                return dispatch['tens']()
            elif n < 1000:
                return dispatch['hundreds']()
            elif n < 1_000_000:
                return dispatch['thousands']()
            elif n <= 10_000_000:
                return dispatch['millions']()
            else:
                return dispatch['too_large']()

        return retval

    def write_check(self, amount, print_full_message = True):
        words_in_amount =  self.__convert_amount_to_words(amount) \
            if print_full_message else self.__convert_number_to_words(amount)
        print(f"\t{words_in_amount}")

    def __convert_amount_to_words(self, amount):
        dollar_amount = int(amount)
        cents_amount = round((amount - dollar_amount) * 100)
        dollar_words = self.__convert_number_to_words(dollar_amount)
        cent_words = self.__convert_number_to_words(cents_amount)

        return f"The amount ${amount} in words is '{dollar_words} dollars and {cent_words} cents.'"

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 6 - Critical Thinking ***\n')

    try:
     cw = CheckWriter()
     options = [False, True]
     while True:
       amount = float(input('\nEnter amount for check: $'))
       print()
       for option in options:
         cw.write_check(amount, option)
    except Exception as e:
        print(e)

if __name__ ==  '__main__': main()