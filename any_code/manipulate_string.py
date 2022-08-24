from parse import parse

some_text = 'AlaBalaShazam'

mascuerade = "".join('X' if char.isupper() else char for char in some_text)
only_upper = "".join(char for char in some_text if char.isupper())
print(mascuerade)
print(only_upper)

LOG = '[2022] - SALE - PRODUCT: 12345'
FORMAT = '[{date}] - SALE - PRODUCT:{id}'

result = parse(FORMAT, LOG)
print(result)
