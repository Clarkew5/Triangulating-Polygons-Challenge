import sys

class Vertex:
    def __init__(self, name="", colour="uncoloured", connectedVertices=set()):
        self.name = name
        self.colour = colour
        self.connectedVertices = connectedVertices

    def changeColour(self, colour):
        self.colour = colour

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

def testChangeColour():
    A = Vertex("A")
    A.changeColour("red")

    print("Change Colour:\t\t\t", end="")
    if (A.colour == "red"):
        print("PASS")
    else:
        print("FAIL")

def test():
    testVertexConstructors()
    print()
    testChangeColour()

def main():
    polygon = dict()
    polygon["A"] = Vertex("A", "red",           {"B","E","F"})
    polygon["B"] = Vertex("B", "red",           {"A","C","F","G"})
    polygon["C"] = Vertex("C", "yellow",        {"B","D","G","H"})
    polygon["D"] = Vertex("D", "blue",          {"C","H","J"})
    polygon["E"] = Vertex("E", "blue",          {"A","F","I","K"})
    polygon["F"] = Vertex("F", "uncoloured",    {"B","E","F"})
    polygon["G"] = Vertex("G", "uncoloured",    {"B","C","F","H","I","J","M","N"})
    polygon["H"] = Vertex("H", "uncoloured",    {"C","D","G","J","N"})
    polygon["I"] = Vertex("I", "uncoloured",    {"E","F","G","K","L","M"})
    polygon["J"] = Vertex("J", "red",           {"D","H","N","O","S"})
    polygon["K"] = Vertex("K", "yellow",        {"E","I","L","P","T"})
    polygon["L"] = Vertex("L", "uncoloured",    {"I","K","M","P"})
    polygon["M"] = Vertex("M", "uncoloured",    {"G","I","L","N","P","Q"})
    polygon["N"] = Vertex("N", "uncoloured",    {"G","H","J","M","O","Q","R","S"})
    polygon["O"] = Vertex("O", "uncoloured",    {"J","N","R","S"})
    polygon["P"] = Vertex("P", "uncoloured",    {"K","L","M","T","Q"})
    polygon["Q"] = Vertex("Q", "uncoloured",    {"M","N","P","R","T","V"})
    polygon["R"] = Vertex("R", "uncoloured",    {"N","O","Q","S","U","V"})
    polygon["S"] = Vertex("S", "yellow",        {"J","O","R","U"})
    polygon["T"] = Vertex("T", "red",           {"K","R","S","V"})
    polygon["U"] = Vertex("U", "blue",          {"Q","R","S","V"})
    polygon["V"] = Vertex("V", "red",           {"Q", "R", "T", "U"})

if (__name__ == "__main__"):
    if (len(sys.argv) == 2 and sys.argv[1] == '-t'):
        test()
    elif (len(sys.argv) == 1):
        main()
    else:
        print("incorrect input")
