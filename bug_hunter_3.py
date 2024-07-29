def sum_positive_numbers_only(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            number_is_positive = True
            total += number # within the if condition
    return total

numbers_list = [1,-2,3,4,-5,6]
print(sum_positive_numbers_only(numbers_list))