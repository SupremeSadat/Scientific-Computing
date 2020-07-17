class Category:


    def __init__(self, name):
        self.name = name
        self.funds = 0
        self.spent = 0.0
        self.ledger = []

    def check_funds(self, amount):
        if amount > self.funds:
            return False
        else:
            return True

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.funds = self.funds + amount

    def get_balance(self):
        return self.funds

    def transfer(self, amount, towho):
        if amount > self.funds:
            return False
        else:
            self.spent = self.spent + amount
            self.funds = self.funds - amount
            towho.funds = towho.funds + amount
            self.ledger.append({"amount": amount*-1, "description": 'Transfer to ' + towho.name})
            towho.ledger.append({"amount": amount, "description": 'Transfer from ' + self.name})
            return True

    def withdraw(self, amount, description=''):
        self.spent = self.spent + amount
        if amount > self.funds:
            return False
        else:
            self.ledger.append({"amount": amount*-1, "description": description})
            self.funds = self.funds - amount
            return True

    def __str__(self):
        result = self.name.center(30, '*') + '\n'
        for x in self.ledger:
            result = result + x['description'][:23].ljust(23, ' ') + "{:.2f}".format(x['amount']).rjust(7, ' ') + '\n'
        result = result + 'Total: ' + "{:.2f}".format(self.funds)
        return result

def create_spend_chart(categories):
    result = 'Percentage spent by category\n'

    total = sum(x.spent for x in categories)
    percentages = [(x.spent/total)//0.01 for x in categories]
    for x in range(100, -10, -10):
        result = result + str(x).rjust(3, " ") + '|'
        for y in percentages:
            if y >= x:
                result = result + ' o '
            else:
                result = result + '   '
        result = result + ' \n'
    result = result + '    ' + '-'*len(percentages)*3 + '-\n'
    maxLength = max(len(x.name) for x in categories)
    for x in range(maxLength):
        result = result + '    '
        for y in categories:
            if x < len(y.name):
                result = result + ' ' + y.name[x] + ' '
            else:
                result = result + '   '
        result = result + ' \n'
    return result.rstrip() +'  '