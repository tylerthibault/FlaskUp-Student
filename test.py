"""
4 Pillars of OOP
1. Inheritance - building off the parent class 
2. Encapsulation - containing similar code blocks inside a class 
3. Abstraction - removing the details from one class to another
4. Polymorphism - child has the same method name but different logic (could use super() to call on parent class)


class deck, card, player, game

"""

class BankAccount:
    name_of_bank = "Tyler"
    def __init__(self, owner, bal=0):
        self.owner = owner
        self.bal = bal

    def stats(self):
        print(f"owner: {self.owner}")
        print(f"bal: {self.bal}")
        return self

    def change_bal(self, amount, int_rate=0):
        self.bal += amount
        # for i in range(amount):
        #     self.bal += 1


    @classmethod
    def change_bank_name(cls, new_name):
        cls.name_of_bank = new_name
        return cls
        

    @staticmethod
    def do_some_math(x, y):
        """
        It takes something in and it gives something out
        """
        print("I am doing math on an account")


class Savings(BankAccount):
    def __init__(self, owner, bal=0, int_rate=0.4):
        self.int_rate = int_rate
        super().__init__(owner, bal)

    def change_bal(self, amount):
        new_amount = (self.bal * self.int_rate) + amount
        print(f"new amount: {new_amount}")
        super().change_bal(new_amount)
        return self

class Bank:
    def __init__(self):
        self.list_of_accounts = []
    
    def add_account(self, account):
        self.list_of_accounts.append(account)

    def change_account_bal(self, account_idx, amount):
        account = self.list_of_accounts[account_idx]
        account.change_bal(amount)
        return self
    
    def show_stats(self):
        for account in self.list_of_accounts:
            account.stats()
        return self
    

bank1 = Bank()
account1 = Savings("bob")
account2 = BankAccount("tom")

bank1.add_account(account1)
bank1.add_account(account2)


bank1.show_stats()

bank1.change_account_bal(0, 100)
bank1.change_account_bal(0, 100)
bank1.change_account_bal(1, 100)
bank1.change_account_bal(1, 100)



bank1.show_stats()

