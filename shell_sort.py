def sedgewick_gaps(n):
    gaps = []
    k=0
    while True:
        if k % 2==0:
            gap = 9 *(2**k - 2 ** (k // 2)) + 1
        else:
            gap = 8 *2 ** k - 6 * 2 ** ((k + 1) // 2)+1
        if gap>=n:
            break
        gaps.append(gap)
        k += 1

    return gaps[::-1]

def shell_sort(data):
    n = len(data)
    gaps = sedgewick_gaps(n)
    for gap in gaps:
        for i in range(gap, n):
            temp = data[i]
            j=i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
