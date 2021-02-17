import csv

import networkx as nx
import matplotlib.pyplot as plt
import random
import time

import fw
import dijkstra as dj

resultado = dict()

for i in range(5, 150):

    N = i

    matriz_de_adyacencia = list()

    for i in range(N):
        fila = list()
        for j in range(N):
            fila.append(random.randint(0, 1000))
        matriz_de_adyacencia.append(fila)


    print(i)
    start = time.time()
    #dj.dijkstra(matriz_de_adyacencia, src=0, dest=3)
    fw.floydWarshall(matriz_de_adyacencia, N)
    stop = time.time()
    resultado[i] = stop-start

with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in resultado.items():
       writer.writerow([key, value])