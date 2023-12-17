L1 = [1, 3, 5, 7, 9, 14, 17, 19, 24, 30]
L2 = [0, 5, 8, 12, 16, 19, 21, 27, 32, 38]

# Linear Searching


def linear_search(list, search_item):
    found = False
    for i in range(len(list)):
        if search_item == list[i]:
            found = True
            return i
    return -1


a = int(input("Enter the search_item: "))
print(linear_search(L1, a))

# Binary Search


def binary_search(list, search_item):
    min = 0
    max = len(list)
    while min <= max:
        mid = (min + max) // 2
        if search_item == list[mid]:
            return mid
        if search_item < list[mid]:
            max = mid - 1
        if search_item > list[mid]:
            min = mid + 1
    return -1


b = int(input("Enter the search_item: "))
print(binary_search(L2, b))