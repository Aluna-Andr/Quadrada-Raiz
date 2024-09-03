# heap_utils.py

def heapify(vetor, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and vetor[left] > vetor[largest]:
        largest = left

    if right < n and vetor[right] > vetor[largest]:
        largest = right

    if largest != i:
        vetor[i], vetor[largest] = vetor[largest], vetor[i]
        heapify(vetor, n, largest)

def heapify_bottom_up(vetor, i):
    while i > 0:
        p = (i - 1) // 2
        if vetor[p] < vetor[i]:
            vetor[p], vetor[i] = vetor[i], vetor[p]
        else:
            break
        i = p

def makeheap(vetor):
    n = len(vetor)
    for i in range(n // 2 - 1, -1, -1):
        heapify(vetor, n, i)
    return vetor

def removeheap(vetor):
    n = len(vetor)
    if n == 0:
        return None
    vetor[0], vetor[n - 1] = vetor[n - 1], vetor[0]
    maior = vetor.pop()
    if vetor:
        heapify(vetor, len(vetor), 0)
    return maior

