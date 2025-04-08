from itertools import permutations
import random

def Random(Matrix, V, save):
    
    # Creating adjency matrix with edges
    adj = [[] for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if i!=j and Matrix[i][j]==1:
                if j not in adj[i]:
                    adj[i].append(j)
                if i not in adj[j]:
                    adj[j].append(i)

    # Generating tabs used for coloring graph
    FirstColor = [-1 for _ in range(V)]
    SecondColor = [-1 for _ in range(V)]

    # Permutation
    Rans = next(permutations(list(range(V))))
    Rans = tuple(next(permutations(list(range(V)))))
    Rans = list(Rans)
    random.shuffle(Rans)
    Rans = tuple(Rans)
    print("Permutation: ", Rans)

    # Setting color for first vertex
    FirstColor[Rans[0]] = 0
    SecondColor[Rans[0]] = 1

    # Tab for currently using colors by neighbours
    available = [False for _ in range(V*V)] # V^2 max number of colors
    numofcolors = 0

    for vertex in range(1, V):

        # Setting avaible colors
        for i in adj[Rans[vertex]]:
            if (FirstColor[i] != -1):
                available[FirstColor[i]] = True
            if (SecondColor[i] != -1):
                available[SecondColor[i]] = True

        # Searching for first color
        seraching = 0
        while seraching < V*V:
            if not available[seraching]:
                break
            seraching += 1
			

        FirstColor[Rans[vertex]] = seraching 
        available[seraching] = True

        if(seraching  > numofcolors):
            numofcolors = seraching

        # Searching for second color
        seraching = 0
        while seraching < V*V:
            if not available[seraching]:
                break
            seraching += 1
            
        SecondColor[Rans[vertex]] = seraching
        available[seraching] = True

        if(seraching  > numofcolors):
            numofcolors = seraching
        
        available = [False for _ in range(V*V)]

    ColorsID = []
    for vertex in range(V):
        ColorsID.append( (FirstColor[vertex],SecondColor[vertex]) ) 
    ColorsNUMS = numofcolors+1

    save["ChromaticNum"] = ColorsNUMS
    save["Colors"] = ColorsID
