import sys

class Vertex:
    def __init__(self, name="", colour="uncoloured", connectedVertices=set()):
        self.name = name
        self.colour = colour
        self.connectedVertices = connectedVertices

def testVertexConstructors():
    print("Vertex Constuctor Tests")

    #default case tests
    defaultV = Vertex()
    print("\tDefault Name:\t\t", end="")
    if (defaultV.name == ""):
        print("PASS")
    else:
        print("FAIL")

    print("\tDefault Colour:\t\t", end="")
    if (defaultV.colour == "uncoloured"):
        print("PASS")
    else:
        print("FAIL")

    print("\tDefault Vertices:\t", end="")
    if (defaultV.connectedVertices == set()):
        print("PASS")
    else:
        print("FAIL")

    #set case tests
    setV = Vertex("A", "red", {"B", "C"})
    print("\tSet Name:\t\t", end="")
    if (setV.name == "A"):
        print("PASS")
    else:
        print("FAIL")

    print("\tSet Colour:\t\t", end="")
    if (setV.colour == "red"):
        print("PASS")
    else:
        print("FAIL")

    print("\tSet Vertices:\t\t", end="")
    if (setV.connectedVertices == {"B", "C"}):
        print("PASS")
    else:
        print("FAIL")

def test():
    testVertexConstructors()

if (__name__ == "__main__"):
    if (len(sys.argv) == 2 and sys.argv[1] == '-t'):
        test()
    else:
        print("incorrect output")
