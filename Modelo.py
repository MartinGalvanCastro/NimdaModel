# ----------------------------------------------------
# Abstract NIMFA Model
# Author: Martin Galvan
# Abstract NIMFA Model
# Version: 1.0
# ----------------------------------------------------

from abc import ABC,abstractclassmethod
from Graph import Graph
import matplotlib
import numpy as np
from random import uniform, seed
import matplotlib as mpl
from matplotlib import pyplot as plt
from os import environ

rngSeed = 32
np.random.seed(rngSeed)
seed(rngSeed)

matplotlib.use('QT5Agg')

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

suppress_qt_warnings()


class NIMFA:

    def __init__(self, adjMatrix: np.array, graph: Graph) -> None:
        """
        Funcion de inicializacion del modelo NIMFA
        """
        self.adjMatrix = adjMatrix
        self.n = len(self.adjMatrix)
        self.m = 10
        self.h = 1
        self.T = round(self.m/self.h)
        self.v = np.zeros((self.n, self.T))
        self.colors = mpl.colors.Normalize(vmin=0, vmax=1, clip=True)
        self.v[:, 0] = [uniform(0, 0.05) for _ in range(self.n)]
        self.graph = graph
        self.degrees = self.graph.get_degree_of_nodes()
        self.nodes_infected = []

    def setRates(self,delta,beta):
        """
        Funcion para definir las tasas de infeccion del modelo
        """
        self.beta = beta
        self.delta = delta


    @abstractclassmethod
    def run(self):
        """
        Funcion que soluciona el modelo NIMFA
        """
        pass
        
            

    def matrixMul(self, matrixArray: list) -> np.array:
        """
        Metodo que multiplica las matrices del arreglo
        """
        resultado = matrixArray[0]
        for i in range(1, len(matrixArray)):
            resultado = np.matmul(resultado, matrixArray[i])
        return resultado

    def checkLimit(self, v: np.array) -> np.array:
        """
        Metodo que valida si el resultado esta dentro del limite
        """
        for i in range(self.n):
            if v[i] < 0:
                v[i] = 0
            elif v[i] > 1 - 1/(1 + (self.beta/self.delta)*self.degrees[i][1]):
                v[i] = 1 - 1/(1 + (self.beta/self.delta)*self.degrees[i][1])

        return v

    def plotTime(self):
        """
        Metodo que grafica la evolcion de la infeccion en el tiempo
        """
        plt.figure()
        t = np.linspace(0, self.m, num=len(self.nodes_infected), endpoint=True)
        plt.title('Nodos infectados vs Tiempo')
        plt.xlabel('Instantes de tiempo')
        plt.ylabel('# de nodos infectados')
        plt.plot(t, self.nodes_infected)
        plt.show()
