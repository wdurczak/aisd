  def selection_sort(data):
    
    for i in range (n):
        min_value = data[i]
        for j in range (i+1, n):
            if (data[j]<min_value):
                min_value = data[j]
        min = data.index(min_value)
        data[i], data[min] = min_value, data[i]