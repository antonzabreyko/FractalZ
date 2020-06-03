import io
import csv
import numpy as np

'''Given the input file and the number of additional levels to be generated,
    create a new file called output.frac with the new data.
    @author Anton A. Zabreyko '''

''' Run the program. '''
@staticmethod
def run(file, level, scale_factor, center=None):
    data = readFile(file)

    new_data = fractalAlgorithm(data, scale_factor, center)

    createFile(new_data)

''' Runs the algorithm for given data, scale, and center for one level. '''
@staticmethod
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

    return new_values



''' Reads in a .frac file. '''
@staticmethod
def readFile(file):
    return

''' Creates a new .frac file called "output". '''
@staticmethod
def createFile(newData):
    return


def test():
    data = np.array([[1, 1], [1, -1], [-1, -1], [-1, 1]])
    s = 0.5
    c = [0, 0]
    fracatalAlgorithm(data, s, c)

test()
