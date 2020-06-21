''' Representation and functionality of curve functions. '''

class Curve():

    ''' Takes in a string list  FUNCS containing strings that each represent a function defining the length
        along one axis of a Cartesian coordinate system. '''
    def __init__(self, funcs):
        return



class Function():

    ''' Takes in a string FUNC of the function that the object is to represent. Functions are of the form
        x(t) = ... , where x and t are arbitray and do not have to be named in any particular way, and ... follows
        standard mathematical notation. '''
    def __init__(self, func):
        self.name = func[0]
        self.parameter = func[2]
        self.function = Function.parseFunction(func[6:])

    ''' Recursively parses and returns a Python function that functions identically to the provided function. '''
    def parseFunction(self, func):
        return lambda x: x
