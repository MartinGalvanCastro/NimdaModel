# ------------------------------------------------------------------------------------------------
# Heterogeneous NIMFA model with infection constant as a Poisson Distribution
# Author: Martin Galvan
# Class for making a simulation of NIMFA model with infection constant as a Poisson Distribution
# Version: 1.0
# ------------------------------------------------------------------------------------------------

from pprint import pprint
from Modelo import NIMFA
from Graph import Graph
import numpy as np
from scipy.stats import poisson
from matplotlib import pyplot as plt
import os


class NIMFA_Poisson(NIMFA):

    def __init__(self, adjMatrix: np.array, graph: Graph, delta:int, lamda:int) -> None:
        super().__init__(adjMatrix, graph)
        self.delta = np.ones(shape=(self.n))*delta
        self.lamda = lamda

    def calcularBeta(self):
        self.beta = np.zeros((self.n,self.n))
        for i in range(self.n):
            for j in range(self.n):
                beta = poisson.pmf(self.degrees[i][1],self.lamda)
                self.beta[j,i] = beta*self.adjMatrix[j][i]

    def run(self):
        diff = 1
        self.t=0
        vinit = self.v
        epsilon = 0.0001
        self.calcularBeta()
        pprint(self.beta)
        while diff>epsilon:
            u = np.ones(self.n)
            A = np.diag(u-self.delta)
            B = np.diag(u-vinit)

            C = self.matrixMul([A,vinit])
            D = self.matrixMul([B,self.beta,vinit])

            temp = C+D
            vnext=self.checkLimit(temp)
            diff = np.linalg.norm(vnext - vinit)
            vinit = vnext
            self.nodes_infected.append(len(list(filter(lambda x: x>=0.6,vinit))))

            self.graph.updateValue(vinit)
            self.t+=1

    def checkLimit(self, v: np.array) -> np.array:
        for i in range(self.n):
            if v[i] < 0:
                v[i] = 0
            elif v[i] > 1 - self.delta[i]/(self.delta[i] + np.sum(self.beta[i,:])):
                v[i] = 1 - self.delta[i]/(self.delta[i] + np.sum(self.beta[i,:]))
        return v
    
    def isInSteadyState(self,v)->bool:
        for i in range(self.n):
            if v[i] < 1 - self.delta[i]/(np.sum(self.beta[i,:])):
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
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'JSON/Test10Nodos.json')
    g = Graph(1,path)
    degress = sum(x[1] for x in g.get_degree_of_nodes())/len(g.nodes)
    print(degress)
    model = NIMFA_Poisson(g.adjM,g,0.25,degress)
    model.run()
    model.plotTime()



