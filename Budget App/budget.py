class Category:
    def __init__(self, category):
        self.category = category
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):

        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            self.balance -= amount
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        title_line = "*" * ((30 - len(self.category)) // 2) + self.category + "*" * ((30 - len(self.category)) // 2)
        spending = []
        for stuff in self.ledger:
            temp_spendings = ""
            amount = '{0:.2f}'.format(stuff['amount'])
            description = stuff['description'][:23]

            temp_spendings += description
            temp_spendings += " " * (30 - len(description) - len(amount))
            temp_spendings += amount

            spending.append(temp_spendings)

        return title_line + "\n" + "\n".join(spending) + "\n" + f"Total: {self.balance}"


def create_spend_chart(categories):
    title = "Percentage spent by category"


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([food, entertainment, business]))
expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
print(expected)