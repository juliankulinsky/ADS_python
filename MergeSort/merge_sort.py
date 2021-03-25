def merge_sort(unsorted_list, l=0, r=None):
    """
    Sort an unsorted list with the merging algortihm.

    >>> merge_sort([3, 7, 92, 98, 4, 8, 72, 78])
    [3, 4, 7, 8, 72, 78, 92, 98]
    """

    if r is None:
        r = len(unsorted_list) - 1

    if l < r:
        m = (l+r-1) // 2
        merge_sort(unsorted_list, l, m)
        merge_sort(unsorted_list, m+1, r)
        merge(unsorted_list, l, m, r)

    return unsorted_list


def merge(list, l, m, r):
    divider = m+1
    l_cache = l
    out_list = []

    for i in range(r-l+1):
        if l > m:
            out_list.append(list[divider])
            divider += 1
        elif divider > r:
            out_list.append(list[l])
            l += 1
        elif list[l] < list[divider]:
            out_list.append(list[l])
            l = l + 1
        elif list[l] >= list[divider]:
            out_list.append(list[divider])
            divider += 1

    for i in range(len(out_list)):
        list[i+l_cache] = out_list[i]

    return list

# Test
# print(merge_sort([12, 9, 34, 8, 13, 14, 56, 0.5]))

