class Bank_account:
    def __init__(self, initial_money, limit):
        self.money = initial_money
        self.credit_limit = limit
        self.used_credits = 0
        self.blocked_card = False
    
    def deposit(self, value):
        self.money += value
    
    def withdraw(self, amount):
        if(self.money >= amount):
            self.money -= amount
            print("Sucess")
        else:
            print("Not enought money in your account")
    
    def use_credit_card(self, amount):
        if(not self.blocked_card):
            if(self.credit_limit >= self.used_credits + amount):
                self.used_credits += amount
                print("Sucess")
            else:
                print("Not enought credits")
        else:
            print("You must pay your credit card debt first")

    def credit_payment(self):
        if(self.used_credits > self.money):
            print("Not enought money in your account to pay for your card expenses")
            self.used_credits -= self.money
            self.money = 0
            self.blocked_card = True
            print("You still need to play more " + str(self.used_credits) + " coins")
        else:
            self.money -= self.used_credits
            self.used_credits = 0
            print("You have payed your credit card expenses")
            self.blocked_card = False

        