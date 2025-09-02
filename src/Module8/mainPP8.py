# File: mainPP8.py
# Written by: Angel Hernandez
# Description: Module 8 - Portfolio Project
# Requirement(s):

import os

Terminated_Transaction_Msg = "Transaction terminated."
Retry_ATM_PIN_Reached_Msg = "Retry PIN entry or reject if max attempts reached."

########################## Customer Class ##########################
class Customer:
    Enters_Pin_Msg = "Customer enters PIN."
    Insert_Card_Msg = "Customer inserts card."
    Withdrawal_Request_Msg = "Customer requests withdrawal of $"

    def __init__(self, card_number, pin, account):
        self.pin = pin
        self.error_count = 0
        self.account = account
        self.card_number = card_number

    def insert_card(self):
        print(self.Insert_Card_Msg)

    def enter_pin(self):
        print(self.Enters_Pin_Msg)
        return self.pin

    def request_withdrawal(self, amount):
        if self.account.balance >= amount:
           print(self.Withdrawal_Request_Msg + str(amount))
        else:
            raise Exception(ATM.ATM_Insufficient_Funds_Msg)
        return amount

##########################################################################

########################## ATM Class ##########################
class ATM:
    MAX_ATTEMPTS = 3
    ATM_Dispenses_Cash_Msg = "ATM dispenses $"
    ATM_Prompts_For_Pin_Msg = "ATM prompts for PIN."
    ATM_Insufficient_Funds_Msg = "Insufficient funds."
    ATM_Sufficient_Funds_Msg = "Sufficient funds: OK."
    ATM_Pin_Is_Verified_Msg = "Bank verifies PIN: OK."
    ATM_Verify_Funds_Msg = "ATM checks account balance."
    ATM_Ejects_Card_Msg = "ATM ejects card. Session ended."
    ATM_Pin_Incorrect_Msg = "Bank verifies PIN: Incorrect."
    ATM_Prompt_For_Withdrawal_Msg = "ATM prompts for withdrawal amount."
    ATM_Sends_Pin_To_Bank_Msg = "ATM sends PIN to Bank for verification."
    ATM_Balance_Zero_Closed_Account_Msg = "Balance is zero. Account closed."
    ATM_Retry_Exceeded_Msg = "Error count exceeded. Card retained. Customer rejected."

    def __init__(self, atm_id, location, cash_available):
        self.atm_id = atm_id
        self.location = location
        self.cash_available = cash_available

    def prompt_for_pin(self):
        print(self.ATM_Prompts_For_Pin_Msg)

    def verify_pin(self, entered_pin, correct_pin, customer):
        print(self.ATM_Sends_Pin_To_Bank_Msg)
        if entered_pin == correct_pin:
            print(self.ATM_Pin_Is_Verified_Msg)
            customer.error_count = 0
            return True
        else:
            print(self.ATM_Pin_Incorrect_Msg)
            customer.error_count += 1
            if customer.error_count >= self.MAX_ATTEMPTS:
                print(self.ATM_Pin_Incorrect_Msg)
                return False
            return None

    def prompt_for_amount(self):
        print(self.ATM_Prompt_For_Withdrawal_Msg)

    def verify_funds(self, account, amount):
        print(self.ATM_Verify_Funds_Msg)
        if account.balance >= amount:
            print(self.ATM_Sufficient_Funds_Msg)
            return True
        elif account.balance == 0:
            print(self.ATM_Balance_Zero_Closed_Account_Msg)
            account.is_closed = True
            return False
        else:
            print(self.ATM_Insufficient_Funds_Msg)
            return False

    def dispense_cash(self, amount):
        print(self.ATM_Dispenses_Cash_Msg + str(amount))

    def eject_card(self):
        print(self.ATM_Ejects_Card_Msg)

##########################################################################

########################## Account Class ############################
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.is_closed = False

    def debit(self, amount):
        self.balance -= amount

##########################################################################

###################### Main and Support Methods ##########################

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    try:
        clear_screen()
        print('*** Module 8 - Portfolio Project ***\n')

        # Let's create objects to show the step-by-step flow
        correct_pin = "1234"
        account = Account(account_number="ACNT1234", balance=300)
        customer = Customer(card_number="1234567", pin="1234", account=account)
        atm = ATM(atm_id=111, location="Downtown Seattle", cash_available=4000)

        # Let's print entered details
        print(f"Welcome customer to your branch {atm.location} - ATM ID: {atm.atm_id}. Your account number is {account.account_number}.\n")

        # Steps in sequence
        customer.insert_card()
        atm.prompt_for_pin()
        entered_pin = customer.enter_pin()

        pin_result = atm.verify_pin(entered_pin, correct_pin, customer)
        if pin_result:
            atm.prompt_for_amount()
            amount = customer.request_withdrawal(100)
            if atm.verify_funds(account, amount):
                account.debit(amount)
                atm.dispense_cash(amount)
            atm.eject_card()
        elif pin_result is None:
            print(Retry_ATM_PIN_Reached_Msg)
        else:
            print(Terminated_Transaction_Msg)
    except Exception as e:
        print(e)

if __name__ == '__main__': main()

##########################################################################