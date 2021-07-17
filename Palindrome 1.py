# Our task is to design an optimal algorithm for checking whether a given string is palindrome or not
# palindrome is a string that reads the same forward and backward ex. radar, madam


# This is the easiets way to do it
def palindrome_python(s):
    if s == s[::-1]:  # [::-1] means considering the letters in reverse order
        return True

    return False


if __name__ == '__main__':
    print(palindrome_python('madam'))




