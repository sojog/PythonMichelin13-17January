
def most_frequent_value(numbers):
    
    if not numbers:
      return -1

    # Dictionary of frequencies
    # using dict comprehention
    frequencies_dict = {
      no : numbers.count(no)  for no in numbers if no % 2 == 0
    }

    max_freq = max(frequencies_dict.values())

    if max_freq < 2:
        return -1 

    max_frequencies_array = [f for f in frequencies_dict if frequencies_dict[f] == max_freq]

    return min(max_frequencies_array)



print(most_frequent_value([ 101, 202, 303, 202, 404, 404, 606]))
print(most_frequent_value([ ]))
print(most_frequent_value([ 888, 999, 33, 66 ]))
