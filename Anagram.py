# Construct an algorithm to check the two words are anagram or not

# anagram means we can create a new word from a original word without repeating the letters.

# Original word is called as Subject
# any word that exactly reproduces the letters in another order is anagram
# ex :-   restful-fluster

def is_anagram(str1, str2):

    # if the length of string is different then they are not anagrams
    if len(str1) != len(str2):
        return False

    # we have to sort the letters of the strings and then we have to compare
    # the letters with the same indices
    # this is the bottleneck because it has O(NlogN) time complexity
    str1 = sorted(str1)
    str2 = sorted(str2)

    # after that we have to check the letters with the same indices
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

if __name__ == '__main__':
     s1 = ['f','l','u','s','t','e','r']
     s2 = ['r','e','s','t','f','u','l']

     print(is_anagram(s1, s2))

# Overall running time is O(NlogN)+O(N)=O(NlogN)