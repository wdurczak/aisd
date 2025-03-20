def insertion_sort(data):
    for i in range (1, n):
        for j in range (i-1, 0, -1):
            if (data[j]>data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
