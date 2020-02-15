# insertion sort
def bla(a):
    i = 0
    index = 0
    while i < len(a)-1:
        k = i + 1
        while k < len(a):
            if a[index] > a[k]:
                index = k
            k += 1
        if a[i] > a[index]:
            a[index], a[i] = a[i], a[index]
        i += 1

a = [4, 9, 1, 7, 9, 3, 1, 3, 6, -5]
bla(a)
print(a)