from classes.Entry import Entry

class IncomeEntry(Entry):

    def __init__(self, amount, description, income):
        Entry.__init__(self, amount, description)
        self.income = income

    def get_amount(self):
        return self.amount


