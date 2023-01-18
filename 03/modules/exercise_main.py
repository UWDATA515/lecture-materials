import exercise_fns

def main():
    print(exercise_fns.summary([1, 2, 3]))
    print(exercise_fns.summary([30, 87, 2, 14]))
    print(exercise_fns.is_palindrome('foo'))
    print(exercise_fns.is_palindrome('fooboof'))
    print(exercise_fns.hist({'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}))
    print(exercise_fns.hist({'steve': 'A+', 'susie': 'B', 'sam': 'C', 'sean': 'A+', 'sonya': 'B'}))

if __name__ == '__main__':
    main()
