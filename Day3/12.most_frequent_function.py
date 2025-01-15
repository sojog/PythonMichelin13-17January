"""
Example 1:
Input: nums = []
Output: -1

Example 2:
Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.

Example 3:
Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Example 3:
Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
"""


def most_frequent_value(numbers):
    
    # Check if the list is empty
    if not numbers:
      return -1

    # Dictionary of frequencies
    # using dict comprehention
    frequencies_dict = {
      no : numbers.count(no)  for no in numbers if no % 2 == 0
    }

    max_freq = max(frequencies_dict.values())

    if max_freq == 1:
        return -1 

    max_frequencies_array = [f for f in frequencies_dict if frequencies_dict[f] == max_freq]

    return min(max_frequencies_array)



print(most_frequent_value([ 101, 202, 303, 202, 404, 404, 606]))
print(most_frequent_value([ ]))
print(most_frequent_value([ 888, 999, 33, 66 ]))
