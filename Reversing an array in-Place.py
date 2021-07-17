
def reverse(nums):

    # pointing to the last item
    start_index = 0  # to get the first number
    # pointing to the first item
    end_index = len(nums)-1  # to get the last element of the data structure, (-1) because indexes starts with 0

    while end_index > start_index:
        # we have to keep swapping the elements
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = end_index + 1  # incrementing the stat index
        end_index = start_index - 1  # decrementing the end index

if __name__ == '__main__':

    n = [1, 2, 3, 4]
    a = [-3, 3, 0, -10]
    reverse(n)
    print(n)
    reverse(a)
    print(a)
