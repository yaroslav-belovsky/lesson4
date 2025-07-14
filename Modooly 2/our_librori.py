import random as r
whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation
def genereid_cot(a):
    cod = ""
    for i in range(a):
        cod = cod + r.choice(printable)
    return cod
def calculate(a, b):
        return a + b

if __name__ == '__main__':
    print(calculate(50, 50))
    print("Hello from library")
    print("Main file")
