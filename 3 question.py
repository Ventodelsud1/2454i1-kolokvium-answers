def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


my_list = [1, 2, 4, 5, 6, 3, 4, 3, 5, 1]
print(remove_duplicates(my_list))
