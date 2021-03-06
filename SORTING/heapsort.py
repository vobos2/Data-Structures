
def heap_sort(items):

    if type(items) is list:
        n = len(items)

        # Perform floor division, create max heap
        for i in range(n//2-1, -1, -1):
            # Heapify subtree at index i
            heapify(items, n, i)
        print("max heap", items)
        for i in range(n-1, 0, -1):
            # Swap first and last node
            items[0], items[i] = items[i], items[0]
            # Heapify subtree at index 0
            heapify(items, i, 0)


def heapify(items, n, i):
    '''Heapify will call itself recursively until all parent nodes are greater than their child nodes.'''
    left = 2*i+1
    right = left+1
    maximum = i

    if left < n and items[left] > items[maximum]:
        maximum = left

    if right < n and items[right] > items[maximum]:
        maximum = right

    if maximum != i:
        items[i], items[maximum] = items[maximum], items[i]
        heapify(items, n, maximum)


if __name__ == "__main__":

    item_list = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]

    print(' original  ', item_list)
    heap_sort(item_list)

    print(' sorted  ', item_list)
