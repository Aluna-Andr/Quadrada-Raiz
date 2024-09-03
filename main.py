# main.py

import random
import time
from sorting import sqrtsort_com_heap, insertion_sort
from utils import salvar_em_arquivo

def processar_tamanho(tamanho, metodo_ordenacao):
    intervalo_maximo = tamanho * 10
    vetor_aleatorio = random.sample(range(1, intervalo_maximo), tamanho)

    print(f"Processando vetor de tamanho {tamanho} com {metodo_ordenacao.__name__}...")

    start_time = time.time()
    vetor_ordenado = metodo_ordenacao(vetor_aleatorio.copy())  # Copia para manter o original
    end_time = time.time()

    salvar_em_arquivo(f'vetor_aleatorio_{tamanho}.txt', vetor_aleatorio)
    salvar_em_arquivo(f'vetor_ordenado_{tamanho}.txt', vetor_ordenado)

    print(f"Arquivo 'vetor_aleatorio_{tamanho}.txt' criado com o vetor aleatório.")
    print(f"Arquivo 'vetor_ordenado_{tamanho}.txt' criado com o vetor ordenado.")
    print(f"Tempo de execução para vetor de tamanho {tamanho}: {end_time - start_time:.4f} segundos")


# Definindo tamanhos dos vetores
# tamanhos = [1000, 10000, 100000, 1000000, 10000000]
tamanhos = [1000]

# Testando sqrtsort_com_heap
print("Usando sqrtsort_com_heap:")
for tamanho in tamanhos:
    processar_tamanho(tamanho, sqrtsort_com_heap)

# Testando insertion_sort
print("\nUsando insertion_sort:")
for tamanho in tamanhos:
    processar_tamanho(tamanho, insertion_sort)

