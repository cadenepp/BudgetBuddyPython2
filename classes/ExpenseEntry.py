from classes.Entry import Entry

class ExpenseEntry(Entry):

    def __init__(self, amount, description):
        Entry.__init__(self, amount, description)

    def get_amount(self):
        return self.amount