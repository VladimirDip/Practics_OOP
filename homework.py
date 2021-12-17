import datetime as dt


class Calculator:
    def __init__(self, limit):
        """Indificate base class"""
        self.limit = limit
        self.records = []

    def add_record(self, new_item):
        """Add to records new spend of the day"""
        self.records.append(new_item)

    def get_today_stats(self):
        """Function for check how much amount in day"""
        today = dt.datetime.now().date()
        count = 0
        for item in self.records:
            if item.date == today:
                count_spend = item.amount
                count += count_spend
        return count

    def get_week_stats(self):
        """Find to spend count on the week"""
        long_week = dt.datetime.now().date() - dt.timedelta(days=7)
        print(long_week)
        count = 0
        for item in self.records:
            if item.date >= long_week:
                count += item.amount
        return count


class Record:

    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()


class CaloriesCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        if self.limit > self.get_today_stats():
            return f"Сегодня можно съесть что-нибудь ещё," \
                   f" но с общей калорийностью не более {self.limit - self.get_today_stats()} кКал"
        else:
            return f"Хватит есть!"


class CashCalculator(Calculator):
    USD_RATE = 73.83
    EURO_RATE = 83.62
    RUB_RATE = 1

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, valute):
        currency = {
            "rub": [self.RUB_RATE, "руб"],
            "usd": [self.USD_RATE, "USD"],
            "eur": [self.EURO_RATE, "Euro"]
        }
        my_money_valute = self.limit / currency[valute][0]
        my_spend_currency = self.get_today_stats() / currency[valute][0]
        my_remained = abs(my_money_valute - my_spend_currency)

        if my_money_valute > my_spend_currency:
            return f"На сегодня осталось {round(my_remained, 2)} {currency[valute][1]}"
        elif my_money_valute < my_spend_currency:
            return f"Денег нет, держись: твой долг - {round(abs(my_money_valute - my_spend_currency), 2)} " \
                   f"{currency[valute][1]}"
        else:
            return f"Денег нет, держись"


calculator_cash = CashCalculator(1000)
calculator_call = CaloriesCalculator(2000)

r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1500, comment="Наполнение потребительской корзины", date="14.12.2021")
r3 = Record(amount=600, comment="Катание на такси", date="17.12.2021")
r4 = Record(amount=1000, comment="Бар, с друзьями", date="17.12.2021")
calculator_cash.add_record(r1)
calculator_cash.add_record(r2)
calculator_cash.add_record(r3)
calculator_cash.add_record(r4)
calculator_call.get_week_stats()

print(calculator_cash.get_today_cash_remained("rub"))
print()

c1 = Record(amount=500, comment="Пирожёк", date="17.12.2021")
c2 = Record(amount=700, comment="Мороженое", date="17.12.2021")
calculator_call.add_record(c1)
calculator_call.add_record(c2)
print(calculator_call.records[0].date)
print(calculator_call.get_calories_remained())
