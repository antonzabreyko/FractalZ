import io
import csv
import numpy as np

'''Given the input file and the number of additional levels to be generated,
    create a new file called output.csv with the new data.
    @author Anton A. Zabreyko '''
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
            row = N * i + j
            col = j
            A[row][i] += 1
            A[row][col] += s

    offset = np.zeros((N*N, D))
    for i in range(N):
        offset[i] = c

    offset = offset * -s

    new_values = np.dot(A, data) - offset

    print(new_values)





def readFile(file):
    return

def createCSV(newData):
    return

def test():
    data = np.array([[1, 1], [1, -1], [-1, -1], [-1, 1]])
    s = 0.5
    c = [0, 0]
    fractalAlgorithm(data, s, c)

test()
