
# it has O(s) linear running time complexity as far as the number of letters in the string is concerned

def is_palindrome(s):
    original_string = s
    reversed_string = reverse(s)

    if original_string == reversed_string:
        return True

    return False


# O(N) linear running time complexity where N is the number of letters in string s where N = len(s)
def reverse(data):

    # string into a list of characters
    data = list(data)

    # pointing to the last item
    start_index = 0  # to get the first number
    # pointing to the first item
    end_index = len(data) - 1  # to get the last element of the data structure, (-1) because indexes starts with 0

    while end_index > start_index:
        # we have to keep swapping the elements
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index = end_index + 1  # incrementing the stat index
        end_index = start_index - 1  # decrementing the end index

    # Transform the list of letters into string
    return ''.join(data)

if __name__ == '__main__':
    print(is_palindrome('car'))