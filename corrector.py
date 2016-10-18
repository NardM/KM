import re


class Corrector:
    def __init__(self, text):
        self.text = text
        self.words = [x for x in re.findall(r'[A-z\']+', text)]
        self.offers = text.split('.') if '.' in text else '' + text.split('?') if '?' in text else '' + text.split(
            '!') if '!' in text else ''

    def yield_text(self):
        for symbol in self.text[:]:
            yield symbol

    def sss(self):
        def corrector_space(func):
            func()
            punctuation_marks = [',', '.', '?', '!', ':', ';', '-', '(', ')', '\'', '\"', '«', '»']
            for symbol in punctuation_marks:
                self.text = self.text.replace(' ' + symbol, symbol)
                self.text = self.text.replace(symbol, symbol + ' ')
            func()

        @corrector_space
        def corrector_double_space():
            while self.text.find('  ') > 0:
                self.text = self.text.replace('  ', ' ')

    def number_of_brackets(self, symbol):
        meetings = 0
        symbol_count = 0
        for c in self.text:
            if c == '(':
                meetings += 1
            elif c == ')':
                meetings -= 1
                symbol_count += 1
                if meetings < 0:
                    return False

        return meetings == 0


# corrector = Corrector(text)
# corrector.sss()
# print(corrector.text)



def brackets_check(s):
    meetings = 0
    for c in s:
        if c == '(':
            meetings += 1
        elif c == ')':
            meetings -= 1
            if meetings < 0:
                return False

    return meetings == 0


# print("OK" if brackets_check(text) else "FAIL")

text = '''Though. it was winter Vadim Petrovich, the agronomist of the farm, had a busy day last Tuesday.
He began his morning with the radio, he listened to the news. At half past seven he got up, washed, did his morning
exercises at an open window, dressed and had breakfast.
Vadim Petrovich likes mornings, because he can see his family, and he can have a talk with his wife and children.
At a quarter to nine Vadim Petrovich left home. It was a cold winter day. There was a lot of snow on the ground.
The sky wasn't blue, and the sun didn't shine at all. There weren't any people in the street.
Vadim Petrovich went to the farm. It is not far from his house, so he walks there. The road was white with snow and he
couldn't walk fast. When he came to the farm, some people wanted to see and talk to him. His working day began.
At 1 o'clock he went home to have dinner. He had dinner with his wife and little daughter who does not go to school.
He ate his dinner, rested a little, and went back to the farm. Vadim Petrovich had to talk to some people,
to write some letters, and to do some other work. At 5 o'clock he had an important meeting.
And only at 8 o'clock he came home.'''

#offers = text.split('.') if '.' in text else '' + text.split('?') if '?' in text else '' + text.split('!') if '!' in text else ''
for i in range(len(text)):
    if text[i] == '.':
        if i != text.rfind('.'):
            text[i + 2] ='2'

print(text)
