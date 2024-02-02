# You can run this file from the `sample` directory using
# the following command:
#     python -m run.runner
# Note that running the python file directly (instead of
# the module) means the imports won't work. ie you can't
# do the following, because it changes the python path
# to the `run` directory, which can't easily refer to its
# sibling `utils` module:
#     python main.py

from utils.histogram import hist
from utils.palindrome import is_palindrome

def runSomeThings():
    print(is_palindrome('foo'))
    print(is_palindrome('fooboof'))
    print(hist({'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}))
    print(hist({'steve': 'A+', 'susie': 'B', 'sam': 'C', 'sean': 'A+', 'sonya': 'B'}))

if __name__ == '__main__':
    runSomeThings()
