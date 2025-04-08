import time

def CheckColors(Matrix, Vertex, CurrentlyUsed, Checking):
    for i in range(len(Matrix)):
        if Matrix[Vertex][i] == 1 and Checking[i] == CurrentlyUsed:
            return False
    return True

def BruteForce(Matrix, Avaible, FirstColor, SecondColor, Vertex, All, st):
    # Everything Colored
    if Vertex == len(Matrix):
        ans = []
        for i in range(len(FirstColor)):
            ans.append((min(FirstColor[i], SecondColor[i]), max(FirstColor[i], SecondColor[i])))
        All.append(ans)
        return

    # Check the time limit
    if time.time() - st > (5 * 60):
        return

    # If not
    for i in range(Avaible):
        FirstColor[Vertex] = i
        SecondColor[Vertex] = i + 1

        if CheckColors(Matrix, Vertex, i, FirstColor) and CheckColors(Matrix, Vertex, i + 1, SecondColor):
            BruteForce(Matrix, Avaible, FirstColor, SecondColor, Vertex + 1, All, st)

        # Backtrack
        FirstColor[Vertex] = -1
        SecondColor[Vertex] = -1


def Full(Matrix, Avaible, save):
    # Define color tabs
    st = time.time()

    FirstColor = [-1]*len(Matrix)
    SecondColor = [-1]*len(Matrix)

    # Searching for all solutions
    All = []
    BruteForce(Matrix, Avaible, FirstColor, SecondColor, 0, All, st)

    if All:
        # Select the solution with the maximum ChromaticNum
        best_solution = min(All)
        cols = []
        for a,b in best_solution:
            if a not in cols:
                cols.append(a)
            if b not in cols:
                cols.append(b)

        save["ChromaticNum"] = len(cols)+1
        save["Colors"] = best_solution
    else:
        save["ChromaticNum"] = 0
        save["Colors"] = []