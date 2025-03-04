

class Money: 

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    
    def __add__(self, other):
        if self.currency == other.currency:
            total_amount = self.amount + other.amount
            return Money(total_amount, self.currency)
        else:
            raise RuntimeError("Mismatched currency")
        
    def __sub__(self, other):
        if self.currency == other.currency:
            if self.amount >= other.amount:
                self.amount -= other.amount
                return Money(self.amount, self.currency)
            if self.amount < other.amount:
                total_amount = self.amount - other.amount
                return Money(total_amount, self.currency)
        else:
            raise RuntimeError("Mismatched currency")
        
   
    def __mul__(self, factor):
            self.amount *= factor
            return Money(self.amount, self.currency)

        
money1 = Money(25,"US")
money2 = Money(30,"US")

print((money1 - money2).amount)

 

