"""Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element."""


# Initial array
numbers = [ 101, 202, 303, 202, 404, 404, 606]
# Dictionary of frequencies
frequencies = { }

# Iterate through array
for no in numbers:
    # Check if number is even
    if no % 2 == 0 :
        # get the existing value or 0 and add 1 to i
        frequencies[no] =  frequencies.get(no, 0) + 1

# Check all the frequencies
print(frequencies)

# Find maximum frequency value (int)
max_freq = 0
for i in frequencies:
    if frequencies[i] > max_freq:
        max_freq = frequencies[i]
print("Maximul freq", max_freq)

# Find the numers that have the highest frequency found earlier
# defining an array
max_frequencies = []
for f in frequencies:
    if frequencies[f] == max_freq:
        max_frequencies.append(f)

#  Print the numbers that have the highest frequncy
print(max_frequencies )

# Sort the numbers in order to have the smallest numbers on position 0
max_frequencies.sort()
# Get the value on position 0 because this is the smallest
print(max_frequencies[0])

# Find the smallest by using min - built in function
print(min(max_frequencies))