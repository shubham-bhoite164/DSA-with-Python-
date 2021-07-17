# we have to find the duplicates in a one-dimensional array of integers in O(N) running time
# where the integer values are smaller then arrays

# Using the absolute value: with this approach we can achieve O(N) running time algorithm that is in-place as well

def find_duplicates(nums):
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print('Repetition found:%s' % str(abs(num)))


if __name__ == '__main__':
    # This method cannot handle values < 0
    n = [2, 6, 5, 1, 4, 3, 2, 3]
    find_duplicates(n)
