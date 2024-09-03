# sorting.py

import math
from heap_utils import makeheap, removeheap, heapify_bottom_up

def dividir_vetor(vetor):
    n = len(vetor)
    tamanho_parte = math.floor(math.sqrt(n))
    partes = [vetor[i:i + tamanho_parte] for i in range(0, n, tamanho_parte)]
    return tamanho_parte, partes

def sqrtsort_com_heap(vetor):
    _, partes = dividir_vetor(vetor)
    
    heaps = [makeheap(list(parte)) for parte in partes]

    heap_maiores = makeheap([(removeheap(h), i) for i, h in enumerate(heaps)])
    resultado = []
    for _ in range(len(vetor)):
        maior, idx = removeheap(heap_maiores)
        resultado.append(maior)
        if len(heaps[idx]) > 0:
            prox_maior = removeheap(heaps[idx])
            heap_maiores.append((prox_maior, idx))
            heapify_bottom_up(heap_maiores, len(heap_maiores) - 1)
        
    return resultado

def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave
    return vetor

