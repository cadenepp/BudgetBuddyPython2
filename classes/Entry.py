from abc import ABC, abstractmethod

class Entry(ABC):

    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    @abstractmethod
    def get_amount(self):
        pass