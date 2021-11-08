def input_data(count_data):
    list_data = []
    for i in range(count_data):
        list_data += [int(input("Enter DATA [" + str(i+1) + "]: "))]

    return list_data