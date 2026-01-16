import itertools

numbers = [0,1,2,3,4,5,6,7,8,9]
combinations = itertools.combinations(numbers, 3)
combinations_list = list(combinations)
print(combinations_list)
numbers = [1,2,3,4,5,6]
combinations = itertools.combinations(numbers, 4)
combinations_list = list(combinations)
print(combinations_list)