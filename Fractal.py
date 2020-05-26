import io
import csv
import numpy as np

'''Given the input file and the number of additional levels to be generated,
    create a new file called output.csv with the new data. '''
def generateFractals(file, level, scale_factor, center=None):
    data = readFile(file)

    newData = fractalAlgorithm(data, scale_factor, center)

    createCSV(newData)


def fractalAlgorithm(data, s, c):
    N = data.shape[0]
    D = data.shape[1]

    A = np.zeros((N*N, N))

    for i in range(N):
        for j in range(N):
            A[]




def readFile(file):
    return

def fractalAlgorithm(data, center):
    return

def createCSV(newData):
    return
