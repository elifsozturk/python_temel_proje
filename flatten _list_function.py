def flatten_list(list_, flat_list):
    for item in list_:
        if type(item) == list:
            flatten_list(item, flat_list)

        else:
            flat_list.append(item)

    return flat_list

list_ = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_listt = []

print(flatten_list(list_, flat_listt))

