# Import all the required credentials  libraries
import datetime

# characterize a class to represent an ATM account
class ATM_Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        """
        Check out the current balance of the account.
        
        Returns:
            float: The current balance.
        """
        return self.balance

    def withdraw_cash(self, amount):
        """
        Withdraw the cash from the account.
        
        Args:
            amount (float): The amount to withdraw.
        
        Returns:
            bool: True if the withdrawal is successful, False otherwise.
        """
        if amount > self.balance:
            print("Out Of Insufficient funds.")
            return False
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount:.2f} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True

    def deposit_cash(self, amount):
        """
        Deposit the cash into the account.
        
        Args:
            amount (float): The amount to deposit.
        
        Returns:
            bool: True if the deposit is gets successful, False otherwise.
        """
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount:.2f} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True

    def change_pin(self, new_pin):
        """
        Change the PIN Code of the account.
        
        Args:
            new_pin (str): The new PIN Code.
        
        Returns:
            bool: True if the PIN change is successful, False otherwise.
        """
        self.pin = new_pin
        return True

    def get_transaction_history(self):
        """
        Get the transaction details or history of the account.
        
        Returns:
            list: A list of details transaction history entries.
        """
        return self.transaction_history

# characterize a function to simulate the ATM machine
def atm_machine_simulation():
    # Create an ATM account
    account = ATM_Account("1234567890", "1234", 900000)

    while True:
        print("\nATM Machine Simulation")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Current Balance: ${account.check_balance():.2f}")
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: $"))
            if account.withdraw_cash(amount):
                print(f"Withdrawal successful. Remaining balance: ${account.check_balance():.2f}")
            else:
                print("Withdrawal declined.")
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: $"))
            if account.deposit_cash(amount):
                print(f"Deposit successful. New balance: ${account.check_balance():.2f}")
            else:
                print("Deposit declined.")
        elif choice == "4":
            new_pin = input("Enter the new PIN: ")
            if account.change_pin(new_pin):
                print("PIN change successful.")
            else:
                print("PIN change declined.")
        elif choice == "5":
            print("Transaction History:")
            for entry in account.get_transaction_history():
                print(entry)
        elif choice == "6":
            print("Exiting the ATM machine simulation.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the ATM machine simulation
atm_machine_simulation()