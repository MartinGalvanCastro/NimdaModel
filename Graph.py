# ----------------------------------------------------
# Graph creation class
# Author: Martin Galvan
# Class for creating a Graph to emulate an IoT Network
# Version: 1.0
# ----------------------------------------------------

import json
import os
from math import dist, inf
import networkx as nx
import numpy as np
from random import randint, uniform, seed
import matplotlib as mpl
from matplotlib import pyplot as plt


rngSeed = 32
np.random.seed(rngSeed)
seed(rngSeed)

class Graph:
    """
    Clase que crea un grafo y lo grafica
    """

    def __init__(self, mode: int, init: str) -> None:
        """
        Metodo de inicialización del grado
        mode : int
            Modo de creacion:
                1 -> Grafo desde archivo json
                2 -> Grafo Aleatorio
        init : String
            Puede ser la ruta al json o la canitdad de nodos que tiene el grafo
        """

        plt.show()
        self.G = nx.Graph()
        self.graph_data = None
        self.nodes = []
        self.name = ""
        self.colors = mpl.colors.Normalize(vmin=0, vmax=1, clip=True)
        n = 0

        # Cargar matriz desde un JSON
        if mode == 1:
            self.pos = {}
            with open(init) as json_file:
                self.graph_data = json.load(json_file)
                n = len(self.graph_data)
                self.adjM = np.zeros((n, n), int)
                self.nodes = self.graph_data
                for i in range(n):
                    self.pos[i] = self.graph_data[i]['pos']
                    self.adjM[i, :] = self.graph_data[i]["adjList"]
                self.name = init

        # Generar una matriz aleatoria
        elif mode == 2:
            n = int(init)
            RC = 45
            self.pos = {i: (inf, inf) for i in range(n)}
            self.pos[0] = (uniform(0, 100), uniform(0, 100))
            self.adjM = np.zeros((n, n), int)
            self.nodes = [{"value": uniform(0, 0.1), "adjList": [0 for _ in range(n)]}
                          for _ in range(n)]

            # Generar nodos en una posicion
            for i in range(1, n):
                flag = True
                while flag:
                    self.pos[i] = (uniform(0, 100), uniform(0, 100))

                    for j in range(n):
                        if self.pos[j] != (inf, inf) and j != i:
                            dij = dist(self.pos[i], self.pos[j])
                            if dij <= RC:
                                flag = False
                                break

            # Crear lista de adjacencia
            for i in range(n):
                self.nodes[i]["pos"] = self.pos[i]
                for j in range(n):
                    dij = dist(self.pos[i], self.pos[j])
                    if dij <= RC and i != j:
                        self.adjM[i, j] = 1
                        self.nodes[i]["adjList"][j] = 1

        self.graph_data = self.nodes
        for i in range(n):
            for j in range(i+1, n):
                if self.adjM[i, j] == 1:
                    self.G.add_edge(i, j)
        nx.set_node_attributes(
            self.G, {i: self.nodes[i]['value'] for i in range(n)}, name='value')
            # self.save_graph()

        mapper = mpl.cm.ScalarMappable(norm=self.colors, cmap=mpl.cm.coolwarm)
        nx.draw(self.G,
                self.pos,
                node_color=[mapper.to_rgba(self.G.nodes[i]['value'])
                            for i in self.G.nodes],
                with_labels=True,
                font_color='black',
                edge_cmap=mpl.cm.coolwarm,
                vmin=0, vmax=1)
        plt.colorbar(mapper, shrink=0.75)
        plt.draw()

    def updateValue(self, v: np.array) -> None:
        """
        Metodo que actualiza el valor de infección de cada nodo
        ----------
        v : np.array
            Valores para la iteración i
        """
        nx.set_node_attributes(
            self.G, {i: v[i] for i in range(len(v))}, name='value')
        self.plot()

    def plot(self) -> None:
        """
        Metodo para graficar el grafo
        """
        plt.clf()
        mapper = mpl.cm.ScalarMappable(norm=self.colors, cmap=mpl.cm.coolwarm)
        nx.draw(self.G,
                self.pos,
                node_color=[mapper.to_rgba(self.G.nodes[i]['value'])
                            for i in self.G.nodes],
                with_labels=True,
                font_color='black',
                edge_cmap=mpl.cm.coolwarm,
                vmin=0, vmax=1)
        plt.colorbar(mapper, shrink=0.75)
        plt.pause(0.1)
        plt.draw()
        

    def save_graph(self,nombre) -> None:
        """
        Metodo para guardar el grafo en un archivo JSON
        """
        if self.name == '':
            self.name = f"{nombre}.json"
        print("Saving graph as: "+self.name)
        with open(f"{self.name}", "w") as outfile:
            json.dump(self.graph_data, outfile)

    def get_degree_of_nodes(self) -> list:
        """
        Metodo que devuelve el grado de todos los nodos
        """
        return sorted(list(self.G.degree()), key=lambda x: x[0])

    def get_infected_neigboors(self) -> list:
        resp = []
        for node in self.G.nodes():
            adjList = self.graph_data[node]['adjList']
            infected = 0
            for i,neighboor in enumerate(adjList):
                if neighboor==1:
                    infected += 1 if self.G.nodes[i]['value']>=0.65 else 0
            resp.append((node,infected))
        return resp

if __name__=='__main__':
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'JSON')
    for i in range(10,20):
        g = Graph(2,f'{i}')
        g.save_graph(f'{path}/Test{i}Nodos')
    