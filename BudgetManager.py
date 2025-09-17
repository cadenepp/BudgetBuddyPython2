
class BudgetManager:
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, income):
        self.incomes.append(income)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_income(self):
        total = 0
        for income in self.incomes:
            total += income.get_amount()
        return total

    def get_total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense.get_amount()
        return total

    def get_net_total(self):
        total = self.get_total_income() - self.get_total_expense()
        return total