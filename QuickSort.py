def quickSort(l, h):
    if l < h:
        j = partition(l, h)

        quickSort(l, j)
        quickSort(j + 1, h)

    return a


def partition(l, h):
    pivot = l
    l = l + 1
    while (l <= h):
        if a[l] <= a[pivot]:
            l += 1

        elif a[h] > a[pivot]:
            h -= 1

        else:
            a[l], a[h] = a[h], a[l]
    if h != pivot:
        a[h], a[pivot] = a[pivot], a[h]
    return pivot


a = [4, 2, 7, 8, 12, 8, 16, 18, 7, 23, 9, 54, 1, 65, 2, 57]
print(quickSort(0, len(a) - 1))
