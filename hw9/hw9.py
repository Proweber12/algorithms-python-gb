from random import sample

number_lists = [sample(range(-30, 30), 4), sample(range(-30, 30), 4), sample(range(-30, 30), 4), sample(range(-30, 30), 4)]

print(number_lists)

min_value = []

for i in range(len(number_lists)):
    min_el = number_lists[i][0]
    for j in range(len(number_lists[i])):
        if min_el > number_lists[i][j]:
            min_el = number_lists[i][j]
    min_value.append(min_el)

max_el = min_value[0]

for x in min_value:
    if max_el < x:
        max_el = x

print(min_value)
print(max_el)