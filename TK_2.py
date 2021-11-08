def tuple_minmax(list_data):
    _min = list_data[0]
    _max = list_data[0]
    for i in range(len(list_data)):
        if _min > list_data[i]:
            _min = list_data[i]
        if _max < list_data[i]:
            _max = list_data[i]
    min_max = (_min, _max)
    return min_max