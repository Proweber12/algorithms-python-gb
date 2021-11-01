from random import sample

number_lists = [sample(range(-30, 30), 4), sample(range(-30, 30), 4), sample(range(-30, 30), 4), sample(range(-30, 30), 4)]

print(number_lists)

for index_lists, lists in enumerate(number_lists):
    number_sum = 0
    for index_num, num in enumerate(lists):
        number_sum += number_lists[index_lists][index_num]
    number_lists[index_lists].append(number_sum)

print(number_lists)

print(f'\n Разделение \n')
