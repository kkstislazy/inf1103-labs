from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float: 
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float) -> None:
        self.__percent = percent

    def apply(self, total: float) -> float:
        return total - (total*(self.__percent/100))

class BulkDiscount(DiscountStrategy): 
    def __init__(self, threshold: float, amount: float) -> None:
        self.__threshold = threshold
        self.__amount = amount
    def apply(self, total: float) -> float: 
        if total < self.__threshold: 
            return total 
        elif total >= self.__threshold: 
            return total - self.__amount

class  StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float: 
        return total - (total*0.05)
