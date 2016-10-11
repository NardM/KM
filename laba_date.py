class labaDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __add__(self, other):
        self.day += other
        self.select_month_add()
        return labaDate(self.day, self.month, self.year)

    def __sub__(self, other):
        self.day -= other.day
        self.month -= other.month
        self.year -= self.year
        self.select_month_sub()
        return labaDate(self.day, self.month, self.year)

    def select_month_add(self):
        month_31 = [1, 3, 5, 7, 8, 10, 11]
        month_28_30 = [2, 4, 6, 9, 12]
        while self.day >= 28:
            if self.month in month_31:
                if self.day > 31:
                    self.month, self.day = self.month + 1, self.day % 31
                else:
                    break
            if self.month in month_28_30:
                if self.month == 2 and self.day > 28:
                    self.month, self.day = self.month + 1, self.day % 28
                else:
                    break

        while self.month > 12:
            if self.month > 12:
                self.month, self.year = self.month % 12, self.year + 1

    def select_month_sub(self):
        month_31 = [1, 3, 5, 7, 8, 10, 11]
        month_28_30 = [2, 4, 6, 9, 12]
        while self.day<0:
            if self.month in month_31:
                if self.day < 0:
                    self.month, self.day = self.month - 1, self.day + 31
                else:
                    break
            if self.month in month_28_30:
                if self.day < 0 and self.month == 2:
                    self.month, self.day = self.month - 1, self.day + 28
                if self.day < 0:
                    self.month, self.day = self.month - 1, self.day + 30
                else:
                    break

        while self.day<0:

    def __str__(self):
        return '{}.{}.{}'.format(self.day, self.month, self.year)


def convert_in_date(line_date):
    day, month, year = map(int, line_date.split('.'))
    return day, month, year


a = labaDate(11, 11, 2016)
b = labaDate(12, 8, 2015)
print(a - b)
# print(s.__str__())

# print(convert_in_date('02.05.2015'))
