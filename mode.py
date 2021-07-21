"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""

    #edge case: if list is empty, return None

    #initialize empty set: mode_set
    #initialize empty dictionary: mode_dictionary

    #add each number to dictionary as the key and increment the value depending
    #on how frequently it appears in the list

    #sort dictionary by doing the following:
    #create a new counts_list
    #for each num, count, in dictionary, add a tuple to counts list:
        #tuple is (count, num)

    #sort counts list.

    #add first tuple, index 1 to our mode_set

    #iterate over counts list:
        #if count == count[0]:
            #add the corresponding number to our mode_set

    #return mode set

    if nums == []:
        return None

    mode_set = set()
    mode_dictionary = {}

    for num in nums:
        mode_dictionary[num] = mode_dictionary.get(num, 0) + 1

    highest_count = max(mode_dictionary.values())

    for num, count in mode_dictionary.items():
        if count == highest_count:
            mode_set.add(num)

    return mode_set



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
