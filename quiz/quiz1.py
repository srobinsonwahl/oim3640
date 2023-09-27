# 1. Currency conversion:
def convert(usd, currency):
    if currency == str('EUR'):
        return usd * 0.94
    elif currency == str('CNY'):
        return usd * 7.29
    elif currency == str('JPY'):
        return usd * 147.71
    else:
        print('Enter a valid currency')

print(convert(46.00, 'EUR'))

# 2. Pattern printer
def pattern(n):
    for i in range(1, n + 1):
        print('*' * i) # Not sure if I wrote i or n here on paper

pattern(4)