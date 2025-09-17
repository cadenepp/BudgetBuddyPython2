from classes.Entry import Entry

class ExpenseEntry(Entry):

    def __init__(self, amount, description, expense):
        Entry.__init__(self, amount, description)
        self.expense = expense

    def get_amount(self):
        return self.amount