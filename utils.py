#/tesis/Scripts python
# ----------------------------------------------------
# Utils functions
# Author: Martin Galvan
# Version: 1.0
# ----------------------------------------------------

import json
import os
import optparse
from pprint import pprint
import pandas as pd
import numpy as np

JSONPath = os.path.abspath('JSON')
XLSXPath = os.path.abspath('XLSX')
DATPath = os.path.abspath('DAT')


def JSONtoXlsx(jsonRoute, xlsxRoute):
    """
    Metodo que lee el archivo JSON, y lo vuelve un archivo xlsx para 
    poder ser leido por el simulador de Jose
    """

    jsonFile = open(jsonRoute)
    graph = json.load(jsonFile)
    n = len(graph)
    adjMatrix = np.zeros(shape=(n+1,n))
    adjMatrix[0,:] = [i for i in range(1,n+1)]
    for index, node in enumerate(graph):
        adjMatrix[1:,index] = node['adjList']
    excelFile = pd.DataFrame(data=adjMatrix)
    excelFile.to_excel(xlsxRoute)


def JSONtoEdgesList(jsonRoute, listRoute):
    """
    Metodo que lee el archivo JSON, y lo vuelve un archivo dat para
    poder ser leido por el simulador de Gillepse
    """
    with open(listRoute,'w') as datFile:
        jsonFile = open(jsonRoute)
        graph = json.load(jsonFile)
        for i, node in enumerate(graph,start=1):
            adjList = node['adjList']
            for j, adjNode in enumerate(adjList,start=1):
                if adjNode==1:
                    datFile.write(f'{i},{j}\n')



def parseOptions():
    optParser = optparse.OptionParser()
    optParser.add_option('-t', '--transform', action='store', type='int', dest='transformation',
                         help='Type of transformation, from JSON to: \n 1.XLSX \n 2.dat ')
    optParser.add_option('-o', '--origin', action='store', type='string',
                         dest='origin', help='Name of the JSON file')
    optParser.add_option('-d', '--destinantio', action='store',
                         type='string', dest='dest', help='Name for the transformed file')
    opts, args = optParser.parse_args()

    return opts


if __name__ == "__main__":
    opts = parseOptions()
    origin = str(opts.origin)+".json"
    dest = str(opts.dest)
    if origin and dest:
        if opts.transformation == 1:
            JSONtoXlsx(os.path.join(JSONPath,origin), os.path.join(XLSXPath,dest+'.xlsx'))
        elif opts.transformation == 2:
            JSONtoEdgesList(os.path.join(JSONPath,origin), os.path.join(DATPath,dest+'.dat'))
        else:
            raise Exception('It was not inputed the correct transformation')
    else:
        raise Exception(
            'It was not specified the origin, or destination route')