def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index=i
        for j in range(i+1, n):
            if data[j]<data[min_index]:
                min_index=j
        data[i],data[min_index] = data[min_index], data[i]