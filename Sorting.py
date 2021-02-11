L1 = [19, 24, 1, 3, 5, 17, 30, 7, 9, 14]
L2 = [0, 16, 19, 21, 5, 8, 12, 27, 32, 38]

# Bubble Sorting


def bubble_sort(list):
    swap = True
    while swap:
        swap = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1],  list[i]
                swap = True
    return list


print(f"Before sorting, list: {L1}")
print(f"After sorting, list: {bubble_sort(L1)}")

# Selection Sorting


def selection_sort(list):
    for i in range(len(list)):
        min_position = i
        for j in range(i + 1, len(list)):
            if list[min_position] > list[j]:
                min_position = j
        list[i], list[min_position] = list[min_position], list[i]
    return list


print(f"Before sorting, list: {L2}")
print(f"After sorting, list: {selection_sort(L2)}")

# Insertion Sorting


def insertion_sort(list):
    for i in range(1, len(list)):
        current = list[i]
        while i > 0 and list[i - 1] > current:
            list[i], list[i - 1] = list[i - 1], list[i]
            i = i - 1
    return list


print(f"Before sorting, list: {L1}")
print(f"After sorting, list: {insertion_sort(L1)}")


# Merge Sorting


def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        # recursion
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i = i + 1
            else:
                list[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left) :
            list[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            list[k] = right[j]
            j = j + 1
            k = k + 1
    return list


print(f"Before sorting, list: {L2}")
print(f"After sorting, list: {merge_sort(L2)}")