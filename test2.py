# ctrl + / 줄 주석
# list_of_list = [
#     [1, 2, 3],
#     [4, 5, 6, 7],
#     [8, 9],
# ]

# for a in list_of_list:
#     # list_of_list를 반복을 돌려서 a라는 변수에 넣는다.
#     # [1, 2, 3] > [4, 5, 6, 7] > [8, 9]
#     for b in a:
#         # 다시 a라는 변수를 반복을 돌려 b라는 변수에 넣는다.
#         # 1, 2, 3 / 4, 5, 6, 7 / 8, 9
#         print(b)
    

# (1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'tuple'>  튜플 (값을 변경할 수 없음)
# {1, 2, 3, 4, 5, 6, 7, 8, 9} 딕셔너리(dict)
# [1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>  리스트(list)

# abc = {'1':'2', '5':'7'}
# print(type(abc))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# output = [[], [], []]
#
# print(len(numbers))
#
# for number in numbers:
#     output[(number + 2) % 3].append(number)
#
# print(output)

aaa = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
output = []

for subList in aaa:
    for list in subList:
        output.append(list)
output.sort(reverse=True)  # 내림차순 desc

print(output)

# for b in aaa:
#     for c in b:
#         output[c % 1].append(c)

# print(3 % 3)

# output[(number - 1) % 3].append(number)

# 0, 1, 2, 3, 4, 5, 6, 7, 8
# 0, 1, 2, 0, 1, 2, 0, 1, 2

# [1, 4, 7] [2, 5, 8] [3, 6, 9]