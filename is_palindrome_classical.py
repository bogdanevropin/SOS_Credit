"""
Checking if string is palindrome (4 min)
"""


def palindrome_check(phrase):
    """
    checks if this string is palindrome
    :param phrase:
    :return: True (palindrome) or False (Not palindrome)
    """
    return phrase == phrase[::-1]


def main():
    """
    Start checking
    """
    s = input('Input string for palindrome checking (only letters)\n')
    if s.isalpha():
        if palindrome_check(s):
            print(f'{s} is palindrome')
        else:
            print(f'{s} is not palindrome')


if __name__ == '__main__':
    main()
