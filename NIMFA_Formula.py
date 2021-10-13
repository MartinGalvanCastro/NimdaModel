# -------------------------------------------------------------------------------------------------------------
# Heterogeneous NIMFA model with infection constant as a relation betweeen current I and P
# Author: Martin Galvan
# Class for making a simulation of NIMFA model with infection constant as a relation betweeen current I and P
# Version: 1.0
# -------------------------------------------------------------------------------------------------------------

from Modelo import NIMFA
from Graph import Graph
import numpy as np

class NIMFA_Fixed(NIMFA):

    def __init__(self, adjMatrix: np.array, graph: Graph, delta:int) -> None:
        super().__init__(adjMatrix, graph, delta)
        self.betaI = 0.006

    def calcularBeta(self):
        self.beta = (self.betaI/2)

    def run(self):
        pass