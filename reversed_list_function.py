def reversed_list(list, reverse_list):
    reverse_list = [i[::-1] for i in list]
    return reverse_list[::-1]

list = [[1, 2], [3, 4], [5, 6, 7]]
revers_list = []
print(reversed_list(list, revers_list))
