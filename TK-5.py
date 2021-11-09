import math
def square_root(list_data):
    new_list = []
    for i in list_data:
        if i>0:
            new_list.append(math.sqrt(i))
        else:
            new_list.append("No")
    return new_list