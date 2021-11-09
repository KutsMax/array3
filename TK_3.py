from statistics import mean

def divide_by_avg(list_data):
    avg = mean(list_data)
    new_list = []
    for i in list_data:
        i = i/avg
        new_list.append(i)
    return new_list