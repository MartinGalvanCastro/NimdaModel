# -----------------------------------------------------------------
# NIMFA Model with Fixed constant from previous project
# Author: Martin Galvan
# Class for making a simulation of NIMFA model with fixed constant
# Version: 1.0
# -----------------------------------------------------------------

from Modelo import NIMFA
from Graph import Graph
import numpy as np

class NIMFA_Fixed(NIMFA):

    def __init__(self, adjMatrix: np.array, graph: Graph, delta:int) -> None:
        super().__init__(adjMatrix, graph,delta)
        self.beta = 1.8 #Infeccion
        self.delta = 0.1 #Cura

    def run(self):
        pass
