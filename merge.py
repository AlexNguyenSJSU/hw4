def merge (list_1, list_2):
    result = []
    i = j = 0

    # Comparing these 2 input lists:
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    # Checking the remaining elements of both lists:
    while i < len(list_1):
        result.append(list_1[i])
        i += 1

    while j < len(list_2):
        result.append(list_2[j])
        j += 1

    return result
