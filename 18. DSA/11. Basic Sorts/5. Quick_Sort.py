def swap(my_list, index1, index2):
    """
    Function to swap variable of given indices of a list.
    """
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    """
    pivot function only returns the swap index. which is 
    the index of value where all the values of  left part of the list  is less and right part is 
    greater than the swap_index value.
    """
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


# my_list = [4, 6, 1, 7, 3, 2, 5]

# print(pivot(my_list, 0, 6))
# print(my_list)


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
