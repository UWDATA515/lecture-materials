# You can run this file from the `sample` directory using
# either of the following two commands:
#     python main.py
# or
#     python -m main

from utils.histogram import hist
from utils.palindrome import is_palindrome

def main():
    print(is_palindrome('foo'))
    print(is_palindrome('fooboof'))
    print(hist({'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}))
    print(hist({'steve': 'A+', 'susie': 'B', 'sam': 'C', 'sean': 'A+', 'sonya': 'B'}))

if __name__ == '__main__':
    main()
