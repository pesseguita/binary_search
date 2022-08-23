import numpy as np

def binary_search(list_value, number_value):
    value_size = len(list_value)
    # print(value_size)
    middle_position = int(len(list_value)/2)
    print(middle_position)
    print(list_value[middle_position])
    if number_value == list_value[middle_position]:
        print(f'Success {number_value} in {middle_position}')
    elif number_value > list_value[middle_position]:
        print(number_value > list_value[middle_position])
        while number_value != list_value[middle_position]:
            print('still not found')
            middle_position = middle_position + 1
            # number_value_position = list_value.index(number_value)+1
            # print(f'found value in {number_value_position}')
        else:
            print(f'found value in {middle_position}')
    elif number_value < list_value[middle_position]:
        while number_value != list_value[middle_position]:
            print('still not found')
            middle_position = middle_position - 1
            # number_value_position = list_value.index(number_value)+1
            # print(f'found value in {number_value_position}')
        else:
            print(f'found value in {middle_position}')
    else:
        print('something went wrong')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_input = sorted([int(item) for item in input("Enter the list numbers: ").split()])
    number_input = int(input("Enter number for search: "))
    print(list_input)
    binary_search(list_input, number_input)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
