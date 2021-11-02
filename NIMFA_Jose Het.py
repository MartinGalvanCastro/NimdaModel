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
        self.beta = np.zeros((self.n,self.n))
        self.delta = np.ones(shape=(self.n))*delta

    def calcularBeta(self):
        beta = 0.375 #Infeccion
        for i in range(self.n):
            for j in range(self.n):
                self.beta[i,j] = beta*self.adjMatrix[i][j]

    def run(self):
        diff = 1
        self.t = 0
        vinit = self.v
        epsilon = 0.03
        self.calcularBeta()
        t=0
        while diff>epsilon and t<=10:
            u = np.ones(self.n)
            A = np.diag(u-self.delta)
            B = np.diag(u-vinit)

            C = self.matrixMul([A,vinit])
            D = self.matrixMul([B,self.beta,vinit])

            temp = C+D
            vnext=self.checkLimit(temp)
            diff = np.linalg.norm(vnext - vinit)
            print(diff)
            vinit = vnext
            self.nodes_infected.append(len(list(filter(lambda x: x>=0.75,vinit))))
            self.graph.updateValue(vinit)
            t+=1


        self.t = len(self.nodes_infected)


    def checkLimit(self, v: np.array) -> np.array:
        for i in range(self.n):
            if v[i] < 0:
                v[i] = 0
            elif v[i] > 1 - self.delta[i]/(self.delta[i] + np.sum(self.beta[i,:])):
                v[i] = 1 - self.delta[i]/(self.delta[i] + np.sum(self.beta[i,:]))
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
        t = [i for i in range(len(self.nodes_infected))]
        print(t)
        plt.title('Nodos infectados vs Tiempo')
        plt.xlabel('Instantes de tiempo')
        plt.ylabel('# de nodos infectados')
        plt.plot(t, self.nodes_infected)
        plt.grid(True)
        plt.show()

if __name__=='__main__':
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'JSON/Test10Nodos.json')
    g = Graph(1,path)
    model = NIMFA_Fixed(g.adjM,g,0.2)
    model.run()
    model.plotTime()