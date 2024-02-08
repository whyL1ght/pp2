def find_common_elements(list1, list2):
    common_elements = [element for element in list1 if element in list2]
    return common_elements

list1 = input().split()
list2 = input().split()
common_elements = find_common_elements(list1, list2)
print(common_elements)