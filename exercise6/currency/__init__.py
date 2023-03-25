class ccy(object):
    def __init__(Self, value: float, currency: str = "EUR"):
        if not isinstance(currency, str):
            raise TypeError("Currency is not a string and it should be you NOOB!")
        if not (currency is "EUR" or currency is "USD" or currency is "CAD" or currency is "JPY"):
            raise ValueError("Incorrect currency. What the hell are you paying with?")
        Self.value = value
        Self.currency = currency
    
    def __add__(Self, other) -> float:
        def currencyToEuro(currency):
            if currency is "USD":
                return 1.06
            elif currency is "CAD":
                return 1.46
            elif currency is "JPY":
                return 140.6
        
        if Self.currency is not "EUR":
            retValue = Self.value / currencyToEuro(Self.currency)
        else:
            retValue = Self.value
        
        if other.currency is not "EUR":
            retValue += other.value / currencyToEuro(other.currency)
        else:
            retValue += other.value
        
        if Self.currency is not "EUR":
            return ccy(retValue * currencyToEuro(Self.currency), Self.currency)
        return ccy(retValue, Self.currency)
            
