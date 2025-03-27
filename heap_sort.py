def heapify(inpt, size, root):
    max_idx = root
    left = 2 *root+ 1
    right = 2 *root+2
    if left< size and inpt[root] < inpt[left]:
        max_idx = left
    if right<size and inpt[max_idx] < inpt[right]:
        max_idx = right
    if max_idx != root:
        inpt[root],inpt[max_idx]=inpt[max_idx], inpt[root]
        heapify(inpt,size,max_idx)


def heap_sort(inpt):
    size = len(inpt)
    for i in range(size // 2,-1,-1):
        heapify(inpt,size,i)
    for i in range(size - 1, 0, -1):
        inpt[i],inpt[0] =inpt[0],inpt[i]
        heapify(inpt, i, 0)

