class DifferentCurrencyError(Exception):
    raise ValueError("Those are different currencies")
    

class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """

    def __init__(self, name, code, symbol=None, digits=2):
        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """
        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits


    def __str__(self):
        """
        Should return the currency code, or code with symbol in parentheses.
        """
        if self.symbol is None:
            return f"{self.code}"
        else:
            return f"({self.code} {self.symbol})"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name
                and self.code == other.code and self.symbol == other.symbol
                and self.digits == other.digits)


class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount, currency):
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        Money = []
        self.amount = amount
        self.currency = currency
        if self.amount == int:
            money.append(self.amount)
            
        


    def __str__(self):
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """

        return f"{self.currency.symbol}{self.currency.amount}"

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.amount == other.amount
                and self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        amount = 0
        if self.currency.code == other.curreny.code:
            amount = self.currency.amount + other.currency.amount
            return(amount,self.currency.code)
        else:
            DifferentCurrencyError()

    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        amount = 0
        if self.currency.code == other.currency.code:
            amount = self.currency.amount - other.currency.amount
            return amount,self.curreny.code
        else:
            DifferentCurrencyError()

    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        pass

    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        pass

