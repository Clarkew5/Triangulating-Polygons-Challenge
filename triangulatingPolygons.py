import sys

class Vertex:
    def __init__(self, name="", colour="blank", connectedVertices=set()):
        self.name = name
        self.colour = colour
        self.connectedVertices = connectedVertices

    def changeColour(self, colour):
        self.colour = colour

def findTriangles(polygon):
    triangles = set()
    for vertex in polygon:
        for connectedV in polygon[vertex].connectedVertices:
            if (vertex in polygon[connectedV].connectedVertices):
                verteciesInCommon = polygon[vertex].connectedVertices & \
                                    polygon[connectedV].connectedVertices
                for commonV in verteciesInCommon:
                    triangles.add(frozenset({vertex, connectedV, commonV}))
    return triangles

def triangleCombinatiotns(uncolouredVerticies, colours, properTriangleList, properTriangle):
    if (uncolouredVerticies == set()):
        listTriangle = {}
        for vertex in properTriangle:
            listTriangle[vertex] = properTriangle[vertex]
        properTriangleList.append(listTriangle)
        return
    else:
        for vertex in uncolouredVerticies:
            for colour in colours:
                properTriangle[vertex] = colour
                triangleCombinatiotns(uncolouredVerticies-{vertex}, colours-{colour}, properTriangleList, properTriangle)

def makeProperTriangles(triangle, polygon):
    colours = {"red", "blue", "yellow"}
    coloursUsed = set()
    uncolouredVerticies = set()
    properTriangle = {}
    properTriangleList = []

    for vertex in triangle:
        if (polygon[vertex].colour != "blank"):
            coloursUsed.add(polygon[vertex].colour)
            properTriangle[vertex] = polygon[vertex].colour
        else:
            uncolouredVerticies.add(vertex)

    triangleCombinatiotns(uncolouredVerticies, colours - coloursUsed, properTriangleList, properTriangle)
    return properTriangleList

def triangleConflict(triangle1, triangle2):
    for vertex in triangle1:
        if (vertex in triangle2):
            if (triangle1[vertex] != triangle2[vertex]):
                return True
    return False

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
    if (defaultV.colour == "blank"):
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

def testFindTriangles(testPolygon):
    testTriangles = {frozenset({"A","C","D"}), frozenset({"A","B","D"}),\
                     frozenset({"B","D","E"}), frozenset({"B","E","F"}),\
                     frozenset({"C","D","G"}), frozenset({"D","E","G"}),\
                     frozenset({"E","G","H"}), frozenset({"E","F","H"})}
    print("Find Trinagle:\t\t\t", end="")
    if (testTriangles == findTriangles(testPolygon)):
        print("PASS")
    else:
        print("FAIL")

def testMakeProperTriangles():
    testTriangle = frozenset({"A","B","C"})
    print("Make Trinagle Tesst:")
    print("\tSingle Blank Vertex:\t", end="")
    singleBlankPoly = dict()
    singleBlankPoly["A"] = Vertex("A", "red",   {"B","C"})
    singleBlankPoly["B"] = Vertex("B", "blue",  {"A","C"})
    singleBlankPoly["C"] = Vertex("C", "blank", {"A","B"})
    singleBlankSol = [{"A":"red", "B":"blue", "C":"yellow"}]
    singleBlankTest = makeProperTriangles(testTriangle, singleBlankPoly)
    if(singleBlankTest == singleBlankSol):
        print("PASS")
    else:
        print("FAIL")

    print("\tTwo Blank Vertex:\t", end="")
    twoBlankPoly = dict()
    twoBlankPoly["A"] = Vertex("A", "red",   {"B","C"})
    twoBlankPoly["B"] = Vertex("B", "blank",  {"A","C"})
    twoBlankPoly["C"] = Vertex("C", "blank", {"A","B"})
    twoBlankSol = [{"A":"red", "B":"blue",   "C":"yellow"},\
                   {"A":"red", "B":"yellow", "C":"blue"  }]
    twoBlankTest = makeProperTriangles(testTriangle, twoBlankPoly)
    for dictionarySol in twoBlankSol:
        if (not (dictionarySol in twoBlankTest)):
            print("FAIL")
            return
    print("PASS")

    print("\tThree Blank Vertex:\t", end="")
    threeBlankPoly = dict()
    threeBlankPoly["A"] = Vertex("A", "blank", {"B","C"})
    threeBlankPoly["B"] = Vertex("B", "blank", {"A","C"})
    threeBlankPoly["C"] = Vertex("C", "blank", {"A","B"})
    threeBlankSol = [{"A":"red",    "B":"blue",     "C":"yellow"},\
                     {"A":"red",    "B":"yellow",   "C":"blue"  },\
                     {"A":"blue",   "B":"red",      "C":"yellow"},\
                     {"A":"blue",   "B":"yellow",   "C":"red"   },\
                     {"A":"yellow", "B":"red",      "C":"blue"  },\
                     {"A":"yellow", "B":"blue",     "C":"red"   }]
    threeBlankTest = makeProperTriangles(testTriangle, threeBlankPoly)
    for dictionarySol in threeBlankSol:
        if (not (dictionarySol in threeBlankTest)):
            print("FAIL")
            return
    print("PASS")

def testTriangleConflict():
    print("Triangle Conflict:\t\t", end="")
    t1 = {"A":"red",  "B":"blue",   "C":"yellow"}
    t2 = {"A":"blue", "D":"red",    "E":"yellow"}
    t3 = {"A":"red",  "F":"yellow", "G":"blue"}
    if (triangleConflict(t1, t2) and not triangleConflict(t1, t3)):
        print("PASS")
    else:
        print("FAIL")

def test():
    testPolygon = dict()
    testPolygon["A"] = Vertex("A", "red",     {"B","C","D"})
    testPolygon["B"] = Vertex("B", "blue",    {"A","D","E","F"})
    testPolygon["C"] = Vertex("C", "yellow",  {"A","D","G"})
    testPolygon["D"] = Vertex("D", "blank",   {"A","B","C","E"})
    testPolygon["E"] = Vertex("E", "blank",   {"B","D","F","G","H"})
    testPolygon["F"] = Vertex("F", "yellow",  {"B","E","H"})
    testPolygon["G"] = Vertex("G", "red",     {"C","D","E","H"})
    testPolygon["H"] = Vertex("H", "yellow",  {"G","E","F"})

    testVertexConstructors()
    print()
    testChangeColour()
    print()
    testFindTriangles(testPolygon)
    print()
    testMakeProperTriangles()
    print()
    testTriangleConflict()

def main():
    polygon = dict()
    polygon["A"] = Vertex("A", "red",       {"B","E","F"})
    polygon["B"] = Vertex("B", "red",       {"A","C","F","G"})
    polygon["C"] = Vertex("C", "yellow",    {"B","D","G","H"})
    polygon["D"] = Vertex("D", "blue",      {"C","H","J"})
    polygon["E"] = Vertex("E", "blue",      {"A","F","I","K"})
    polygon["F"] = Vertex("F", "blank",     {"B","E","F"})
    polygon["G"] = Vertex("G", "blank",     {"B","C","F","H","I","J","M","N"})
    polygon["H"] = Vertex("H", "blank",     {"C","D","G","J","N"})
    polygon["I"] = Vertex("I", "blank",     {"E","F","G","K","L","M"})
    polygon["J"] = Vertex("J", "red",       {"D","H","N","O","S"})
    polygon["K"] = Vertex("K", "yellow",    {"E","I","L","P","T"})
    polygon["L"] = Vertex("L", "blank",     {"I","K","M","P"})
    polygon["M"] = Vertex("M", "blank",     {"G","I","L","N","P","Q"})
    polygon["N"] = Vertex("N", "blank",     {"G","H","J","M","O","Q","R","S"})
    polygon["O"] = Vertex("O", "blank",     {"J","N","R","S"})
    polygon["P"] = Vertex("P", "blank",     {"K","L","M","T","Q"})
    polygon["Q"] = Vertex("Q", "blank",     {"M","N","P","R","T","V"})
    polygon["R"] = Vertex("R", "blank",     {"N","O","Q","S","U","V"})
    polygon["S"] = Vertex("S", "yellow",    {"J","O","R","U"})
    polygon["T"] = Vertex("T", "red",       {"K","R","S","V"})
    polygon["U"] = Vertex("U", "blue",      {"Q","R","S","V"})
    polygon["V"] = Vertex("V", "red",       {"Q","R","T","U"})

    triangleSet = findTriangles(polygon)
    triangleList = list(triangleSet)
    for i in range(len(triangleList)):
        properTrianglesList1 = makeProperTriangles(triangleList[i], polygon)
        if (properTrianglesList1 == []):
            continue
        for pTri1 in properTrianglesList1:
            for j in range(i+1, len(triangleList)):
                properTrianglesList2 = makeProperTriangles(triangleList[j], polygon)
                if (properTrianglesList2 == []):
                    break
                otherTriangles = triangleSet-(triangleList[i] | triangleList[j])
                for pTri2 in properTrianglesList2:
                    if triangleConflict(pTri1, pTri2):
                        break
                    if (not fillPolygon(pTri1, pTri2, otherTris, polygon)):
                        break
                    else:
                        print("Solution found")
    print("No solution possible")

if (__name__ == "__main__"):
    if (len(sys.argv) == 2 and sys.argv[1] == '-t'):
        test()
    elif (len(sys.argv) == 1):
        main()
    else:
        print("incorrect input")
