def count_4(lst):
    count = 0
    for num in lst:
        count += str(num).count('4')
    return count

numbers = [4, 24, 42, 14, 34, 404]

result = count_4(numbers)
print("The number 4 appears {} times in the list.".format(result))
