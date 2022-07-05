"""
Checking if string has the same letters (14 min)
"""


def palindrome_check(phrase1, phrase2):
    """
    Checking phrases
    :param phrase1: first string
    :param phrase2: second string
    :return: True if palindromes False if not
    """
    if len(phrase1) != len(phrase2):
        return False
    elif sorted(phrase1) == sorted(phrase2):
        return True
    else:
        return False


def main():
    """
    Start checking
    """
    s1 = input('Input string 1 for palindrome checking (only letters)\n')
    s2 = input('Input string 2 for palindrome checking (only letters)\n')
    if palindrome_check(s1, s2):
        print(f'"{s1}" and "{s2}" are palindromes')
        print(f'Equals {sorted(s1)}')
    else:
        print(f'"{s1}" and "{s2}" are not palindromes')
        print(f'"{sorted(s1)}" not equals "{sorted(s2)}"')


if __name__ == '__main__':
    main()
