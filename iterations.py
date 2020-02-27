# import itertools
#
# counter = itertools.count() # generates an iterable (used only once)
# a = [1, 5, 3, 7, 8]
# b = zip(counter, a)
# print(list(b))
#
# letters = ['a', 'b', 'c', 'd']
# lettercombinations = itertools.combinations(letters,2)
# letterpermutations = itertools.permutations(letters,2)
#
# for item in lettercombinations:
#     print(item)
# for item in letterpermutations:
#     print(item)

piece = 100
for i in range(1, 100):
    print(i, i * piece / 100)
    piece = piece - i * piece / 100
#
# print(list(lettercombinations))
# print(list(letterpermutations))

# for num in counter:
#     print(num)
