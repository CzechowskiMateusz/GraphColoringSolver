import networkx as nx 
import matplotlib.pyplot as plt 

def GraphMaker(data):
    G = nx.Graph()  
    edges = [(i, j) for i, row in enumerate(data) for j, value in enumerate(row) if value == 1]
    G.add_edges_from(edges)
    nx.draw_networkx(G)
    plt.show() 
