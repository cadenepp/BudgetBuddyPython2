from classes.Entry import Entry

class ExpenseEntry(Entry):

    def __init__(self, amount, description, expenses):
        Entry.__init__(self, amount, description)
        self.expenses = expenses

    def get_amount(self):
        return self.amount