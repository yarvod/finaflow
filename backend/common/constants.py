class Currency:
    RUB = 1
    USD = 2
    EUR = 3

    Choices = ((RUB, "руб"), (USD, "usd"), (EUR, "eur"))


class OperationType:
    EXPENDITURE = 1
    REVENUE = 2

    Choices = ((EXPENDITURE, "Расход"), (REVENUE, "Доход"))
