a = [72,6,57,88,60,42,83,73,48,85]

def quickSort(l, r):
    if l >= r:
        return
    else:
        i = l
        j = r
        midValue = a[i]
        while i < j:
            while i < j and a[j] > midValue:
                j = j - 1
            if i < j:
                a[i] = a[j]
                i = i + 1

            while i < j and a[i] < midValue:
                i = i + 1
            if i < j:
                a[j] = a[i]
                j = j - 1
        a[i] = midValue

    quickSort(l, i-1)
    quickSort(i+1,r)

quickSort(0,len(a)-1)
print(a)