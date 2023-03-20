def sort_dictionary (dict):
    sorted_dict_by_age = sorted(dict.items(), key=lambda age: age[1][1], reverse=False)

    result = []

    for name, (phone_num, age) in sorted_dict_by_age:
        tuple_ele = (name, phone_num)
        result.append(tuple_ele)

    return result
