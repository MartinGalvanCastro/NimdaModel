# -----------------------------------------------------------------
# NIMFA Model with Fixed constant from previous project
# Author: Martin Galvan
# Class for making a simulation of NIMFA model with fixed constant
# Version: 1.0
# -----------------------------------------------------------------

import os
from Modelo import NIMFA
from Graph import Graph
import numpy as np
from matplotlib import pyplot as plt

class NIMFA_Fixed(NIMFA):

    def __init__(self, adjMatrix: np.array, graph: Graph, delta:int):
        super().__init__(adjMatrix, graph)
        self.n = len(self.adjMatrix)
        self.beta = 1.8 #Infeccion
        self.delta = delta


    def run(self):
        diff = 1
        self.t = 0
        vinit = self.v
        epsilon = 0.0001
        while diff>epsilon:
            u = np.ones(self.n)
            A = np.diag(np.ones(shape=(self.n))*(1-self.delta))
            B = np.diag(u-vinit)*self.beta

            C = self.matrixMul([A,vinit])
            D = self.matrixMul([B,vinit])

            temp = C+D
            vnext=self.checkLimit(temp)
            diff = np.linalg.norm(vnext - vinit)
            vinit = vnext
            self.nodes_infected.append(len(list(filter(lambda x: x>=0.65,vinit))))

            self.graph.updateValue(vinit)
            self.t+=1


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

    def isInSteadyState(self,v)->bool:
        for i in range(self.n):
            if v[i] < 1/(1 + (self.beta/self.delta)*self.degrees[i][1]):
                return False
        return True

    def plotTime(self):
        """
        Metodo que grafica la evolcion de la infeccion en el tiempo
        """
        plt.figure()
        t = np.linspace(0, self.t, num=len(self.nodes_infected), endpoint=True)
        plt.title('Nodos infectados vs Tiempo')
        plt.xlabel('Instantes de tiempo')
        plt.ylabel('# de nodos infectados')
        plt.plot(t, self.nodes_infected)
        plt.show()

if __name__=='__main__':
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'JSON/TestModelos.json')
    g = Graph(1,path)
    model = NIMFA_Fixed(g.adjM,g,0.25)
    model.run()
    model.plotTime()