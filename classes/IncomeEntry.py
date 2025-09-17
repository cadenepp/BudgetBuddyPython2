from classes.Entry import Entry

class IncomeEntry(Entry):

    def __init__(self, amount, description):
        Entry.__init__(self, amount, description)

    def get_amount(self):
        return self.amount


