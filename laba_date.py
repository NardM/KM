class labaDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.month_31 = [1, 3, 5, 7, 8, 10, 11]
        self.month_30 = [4, 6, 9, 12]

    def __add__(self, other):
        self.day += other
        self.select_month_add()
        return labaDate(self.day, self.month, self.year)

    def __sub__(self, other):
        self.day -= other.day
        self.month -= other.month
        self.year -= other.year
        self.select_month_sub()
        return labaDate(self.day, self.month, self.year)

    def select_month_add(self):
        def month_day(n):
            self.month, self.day = self.month + self.day // n, self.day % n

        def day_month(n):
            self.day, self.month = n, self.month - 1

        while self.day > 28:
            if self.month in self.month_31:
                if self.day > 31:
                    month_day(31)
                if self.day == 0:
                    day_month(31)
            if self.month in self.month_30:
                if self.day > 30:
                    month_day(30)
                if self.day == 0:
                    day_month(30)
            if self.month == 2:
                if self.day > 28:
                    month_day(28)
                if self.day == 0:
                    day_month(28)

        while self.month > 12:
            self.month, self.year = self.month % 12, self.year + self.month // 12

    def select_month_sub(self):
        while self.day < 0:
            if self.month in self.month_31:
                self.month, self.day = self.month - abs(self.day//31), self.day + 31
            if self.month in self.month_30:
                self.month, self.day = self.month - abs(self.day//30), self.day + 30
            if self.month == 2:
                self.month, self.day = self.month - abs(self.day//28), self.day + 28
        while self.month < 0:



    def __str__(self):
        return '{}.{}.{}'.format(self.day, self.month, self.year)


def convert_in_date(line_date):
    day, month, year = map(int, line_date.split('.'))
    return day, month, year


a = labaDate(11, 2, 2016)
print(a + 345)
# print(s.__str__())

# print(convert_in_date('02.05.2015'))
