def remove_negatives(numbers):
    num_list = [item for item in numbers if item >= 0] # Don't remove items from a list you are iterating over as that changes the index of the items and you could end up skipping over some of the elements
    return num_list

numbers_list = [1,-2,3,-4,-5,6,-7,-8]
print(remove_negatives(numbers_list))