
list = ["apple", "banana", "apple", "orange", "banana", "apple"]
def count_fruits(fruits):
    value_of_list = {}
    for fruit in fruits:
        if fruit in value_of_list :
            value_of_list[fruit] += 1
        else:
            value_of_list[fruit] =1
    return value_of_list

    

