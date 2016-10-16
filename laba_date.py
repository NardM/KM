def selection_of_the_month(month):
    month_list = ['None', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
    return month_list[month]


def selection_of_the_day(day):
    if day < 10:
        return '0' + str(day)
    return day


class LabaDate:
    def __init__(self, day, month=None, year=None):
        self.month_31 = [1, 3, 5, 7, 8, 10, 11]
        self.month_30 = [4, 6, 9, 12]
        if isinstance(day, str):
            self.day, self.month, self.year = self.convert_in_date(day)
        else:
            self.day = day
            self.month = month
            self.year = year
        if 12 < self.month or 0 >= self.month:
            raise print('Неправильно введена дата, а именно месяц')
        if 31 < self.day or 0 >= self.day or self.correct_month():
            raise print('Неправильно введена дата, а именно день')
        self.bissextile = 1 if self.bissextile_year() else 0

    def correct_month(self):
        if self.month in self.month_30:
            if self.day > 30:
                return True
        if self.month == 2:
            if self.bissextile_year() and self.day > 29:
                return True
            if self.day > 28 and not self.bissextile_year():
                return True
        return False

    def __add__(self, other):
        self.day += other
        self.select_month_add()
        return LabaDate(self.day, self.month, self.year)

    def __sub__(self, other):
        self.day -= other.day
        self.month -= other.month
        self.year -= other.year
        self.select_month_sub()
        try:
            return LabaDate(self.day, self.month, self.year)
        except BaseException:
            print("Неправильное вычитание")

    def __lt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    return self.day < other.day
                return self.month < other.month
        return self.year < other.year

    def __gt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    return self.day > other.day
                return self.month > other.month
        return self.year > other.year

    def __eq__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                return self.day == other.day

    @staticmethod
    def convert_in_date(line_date):
        return map(int, line_date.split('.'))

    def month_day(self, n):
        self.month, self.day = self.month + self.day // n, self.day % n

    def day_month(self, n):
        self.day, self.month = n, self.month - 1

    def day_month_2(self, n):
        self.month, self.day = self.month - 1, n % self.day

    def select_month_add(self):
        while self.day > 28:
            if self.month in self.month_31:
                if self.day > 31:
                    self.month_day(31)
                if self.day == 0:
                    self.day_month(31)
            if self.month in self.month_30:
                if self.day > 30:
                    self.month_day(30)
                if self.day == 0:
                    self.day_month(30)
            if self.month == 2:
                if self.day > 28 + self.bissextile:
                    self.month_day(28 + self.bissextile)
                if self.day == 0:
                    self.day_month(28 + self.bissextile)
        while self.month > 12:
            self.month, self.year = self.month % 12, self.year + self.month // 12

    def select_month_sub(self):
        while self.day < 0:
            if 12 - abs(self.month) in self.month_31:
                self.day_month_2(31)
                if self.day == 0:
                    self.day_month(31)
            if 12 - abs(self.month) in self.month_30:
                self.day_month_2(30)
                if self.day == 0:
                    self.day_month(30)
            if 12 - abs(self.month) == 2:
                self.day_month_2(28 + self.bissextile)
                if self.day == 0:
                    self.day_month(28 + self.bissextile)
        while self.month < 0:
            self.year, self.month = self.year - 1, 12 - abs(self.month)
            if self.month == 0:
                self.month = 1

    def bissextile_year(self):
        return True if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0 else False

    def __str__(self):
        return '{} {} {}'.format(selection_of_the_day(self.day), selection_of_the_month(self.month), self.year)

    def __repr__(self):
        return '{}.{}.{}'.format(self.day, self.month, self.year)


a = LabaDate(25, 11, 2017)
b = LabaDate(28, 11, 2011)
c = LabaDate('05.11.2107')
print(a - b)

# print(convert_in_date('02.05.2015'))
