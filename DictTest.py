# dict_a = {"name" : "구름"}
#
# del dict_a["name"]
# print(dict_a)

# pets = [
#     {"name": "구름", "age": 5},
#     {"name": "초코", "age": 3},
#     {"name": "아지", "age": 1},
#     {"name": "호랑이", "age": 1}
# ]
#
# print("# 우리 동네 애완 동물들")
# for pet in pets:
#     print("{0} {1}살".format(pet["name"], pet["age"]))

from operator import itemgetter
import random
numbers = []
counter = {}
for i in range(1,21):
    number = random.randint(1,9)
    numbers.append(number)
# numbers.sort()
print(numbers)

# numbers = [1, 5, 7, 5, 5, 7, 5, 6, 9, 4, 7, 8, 2, 2, 4, 6, 4, 4, 6, 4]
# numbers[0] = 1
# numbers[1] = 5
# numbers[2] = 7

# for (int i = 0; i < numbers.length; i++) {
#     int a = numbers[i];
# }

for a in numbers:
    if a in counter:
        counter[a] += 1 # counter[a] = counter[a] + 1
    else:
        counter[a] = 1
scounter = sorted(counter.items())
# scounter = sorted(counter, key = itemgetter(1))
print(scounter)

# print(counter)


