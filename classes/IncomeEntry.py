from classes.Entry import Entry

class IncomeEntry(Entry):

    def __init__(self, amount, description, incomes):
        Entry.__init__(self, amount, description)
        self.incomes = incomes

    def get_amount(self):
        return self.amount


