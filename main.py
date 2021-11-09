import sys
import importlib
from TK_1 import input_data
from TK_2 import tuple_minmax
from TK_3 import divide_by_avg
from TK_4 import multiply_by_avg

def main():
    count = int(input("Enter count data: "))
    list_data = input_data(count)
    print("DATA: ", list_data)
    min_max = tuple_minmax(list_data)
    print("Min and Max of DATA: ", min_max)
    new_list = divide_by_avg(list_data)
    print("Each element is divided by average:", new_list)
    new_list1 = multiply_by_avg(list_data)
    print("Each element is multiplied by average:", new_list1)
    module = importlib.import_module("TK-5")
    new_list2 = module.square_root(list_data)
    print("Square root of each element:", new_list2)
    return 0

if __name__ == "__main__":
    sys.exit(main())