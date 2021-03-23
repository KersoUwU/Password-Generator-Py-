import random
number = '0123456789'
symbols = 'wasdejklopik'
symbolsUp = symbols.upper()
symbolsALL = number + symbols + symbolsUp
print(symbolsALL)
ls = list(symbolsALL)
print(ls)
password = ''.join([random.choice(ls) for x in range(10)])
print(password)