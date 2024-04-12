def unuque (list_):
    unuque_list = []
    for i in list_:
        if i not in unuque_list:
            unuque_list.append(i)
    return unuque_list

print(unuque([1, 2, 2, 3, 1, 5, 6,]))