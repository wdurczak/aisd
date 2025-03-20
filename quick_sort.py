import random

def partition(inpt, mini, maxi):
    pivot = inpt[mini]
    left = mini + 1
    right = maxi
    while True:
        while left <=right and inpt[left] <= pivot:
            left += 1
        while left <=right and inpt[right] > pivot:
            right -= 1
        if left <= right:
            inpt[left], inpt[right] = inpt[right], inpt[left]
        else:
            break
    inpt[mini], inpt[right] =inpt[right], inpt[mini]
    return right

def partition_random(inpt, mini, maxi):
    rand_idx=random.randint(mini, maxi)
    inpt[mini],inpt[rand_idx]= inpt[rand_idx], inpt[mini]
    return partition(inpt, mini, maxi)


def quick_sort(arr, low, high, pivot_type="left"):
    if low < high:
        if pivot_type=="random":
            pivot_idx =partition_random(arr, low, high)
        else:
            pivot_idx =partition(arr, low, high)
        quick_sort(arr,low, pivot_idx - 1, pivot_type)
        quick_sort(arr, pivot_idx + 1, high, pivot_type)

inpt = [12, 11, 13, 5, 6, 7]
print("bazowa tablica: ", inpt)
quick_sort(inpt, 0, len(inpt) - 1, pivot_type="random")
print("posortowana tablica: ", inpt)

