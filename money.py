class Money:
    def __init__(self, rubles, dime=None):
        self.rubles = rubles
        self.dime = dime
        if isinstance(rubles, str):
            self.rubles, self.dime = self.convert_in_money(rubles)
        else:
            self.rubles = rubles
            self.dime = dime

    def __str__(self):
        return '{},{}'.format(int(self.rubles), int(self.dime))

    def __add__(self, other):
        self.rubles += other.rubles
        self.dime += other.dime
        self.select_add()
        return Money(self.rubles, self.dime)

    def __sub__(self, other):
        self.rubles -= other.rubles
        self.dime -= other.dime
        self.select_sub()
        return Money(self.rubles, self.dime)

    def __truediv__(self, other):
        self.rubles /= other.rubles
        self.dime /= other.dime
        self.select_div()
        return Money(self.rubles, self.dime)

    @staticmethod
    def convert_in_money(line_date):
        return map(int, line_date.split(','))

    def select_add(self):
        while self.dime >= 100:
            self.rubles += self.dime // 100
            self.dime %= 100

    def select_sub(self):
        while self.dime < 0:
            self.rubles -= 1
            self.dime += 100
        self.select_add()

    def select_div(self):
        self.dime = self.dime + ((self.rubles - int(self.rubles)) * 100)
        self.select_add()

    def __lt__(self, other):
        if self.rubles==other.rubles:
            return self.dime<other.dime
        return self.rubles < other.rubles


    def __gt__(self, other):
        if self.rubles==other.rubles:
            return self.dime>other.dime
        return self.rubles > other.rubles

    def __eq__(self, other):
        if self.rubles == other.dime:
            return self.dime ==other.dime

a = Money(3, 2)
b = Money(7, 1)
print(a / b)
