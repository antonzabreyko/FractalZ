import io
import csv
import numpy as np

'''Given the input file and the number of additional levels to be generated,
    create a new file called output.frac with the new data. '''

''' Run the program, reading in the given file and outputting new data in a file
    named output.frac. '''
def run(file, scale_factor):
    N, D, L, C, data = readFile(file)

    new_data = fractalAlgorithm(data, scale_factor, C)

    createFile(N, D, L, C, new_data)

''' Runs the algorithm for given data, scale, and center for one level. '''
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
def readFile(file):
    f = open(file, "r")
    text = f.read()
    lines = text.splitlines()

    N, D, L, C = extractFirstLine(lines[0])

    data = extractData(lines[1:])

    return N, D, L, C, np.array(data)


def extractData(lines):
    data = []
    for i in range(len(lines)):
        data.append(parseC(lines[i]))

    return data



''' Extracts fundamental data from the first line. '''
def extractFirstLine(text):
    N = int(text[text.find("N=")+2])
    D = int(text[text.find("D=")+2])
    L = int(text[text.find("L=")+2])
    C = parseC(text[text.find("C=")+3:text.find(")")])

    return N, D, L, C

def parseC(C):
    c_vec = []
    i = 0
    while (i < len(C)):
        if (C[i].isnumeric()):
            c_vec.append(int(C[i]))
        elif C[i] == "-":
            c_vec.append(int(C[i:i+2]))
            i += 1
        i += 1
    return np.array(c_vec)




''' Creates a new .frac file called "output". '''
def createFile(N, D, L, C, newData):
    text = "N=" + str(N) + " D=" + str(D) + " L=" + str(L) + " C=" + str(C) + "\n"
    for i in range(len(newData)):
        text += addLine(newData[i]) + "\n"



    with open("output.frac", "w") as out:
        out.write(text)

    return

def addLine(row):
    text = ""
    for i in range(len(row)-1):
        text += str(row[i]) + ", "

    text += str(row[len(row)-1])
    return text


def test():
    data = np.array([[1, 1], [1, -1], [-1, -1], [-1, 1]])
    s = 0.5
    c = [0, 0]
    fractalAlgorithm(data, s, c)

    run("Test.frac", 0.5)

test()
