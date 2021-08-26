# Heap sort
def heapsort(tmp_arr):
    n = len(tmp_arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(tmp_arr, n, i)  # creating max heap

    for i in range(n - 1, -1, -1):
        # replacing root with last node
        tmp = tmp_arr[i]
        tmp_arr[i] = tmp_arr[0]
        tmp_arr[0] = tmp
        # creating max heap
        heapify(tmp_arr, i, 0)
    return tmp_arr


def heapify(tmp_arr, n, i):
    lc = 2 * i + 1
    rc = 2 * i + 2
    max_num = i
    # check if the left child is greater
    if lc < n and tmp_arr[max_num] < tmp_arr[lc]:
        max_num = lc
    # check if the right child is greater
    if rc < n and tmp_arr[max_num] < tmp_arr[rc]:
        max_num = rc
    # check if we are not at root
    if max_num != i:
        tmp_arr[i], tmp_arr[max_num] = tmp_arr[max_num], tmp_arr[i]
        heapify(tmp_arr, n, max_num)


arr = input().split()
arr = [int(i) for i in arr]  # converting list of string type numbers to int
print(heapsort(arr))
