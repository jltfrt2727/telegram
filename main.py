import string


def sanitize(s):
    return "#" + s.lower().translate(str.maketrans('', '', string.punctuation)).replace(' ', '-')


while True:
    st = input('Enter header: ')
    print('\n')
    print(sanitize(st))
    print('\n')
