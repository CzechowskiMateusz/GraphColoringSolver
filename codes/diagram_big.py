import networkx as nx
import matplotlib.pyplot as plt

ns = [15, 20, 25, 30]

subtitles = ["Algorytm Zachłanny", "Algorytm Zachłanny Losowy", "Algorytm siłowy", "Algorytm genetyczny"]
cols_small_Greedy = [10, 14, 18, 18]
cols_small_Ran = [10, 16, 18, 18]
cols_small_Genetic = [13, 16, 16, 20]

barWidth = 0.2
xpos = list(range(len(ns)))  # Convert the range to a list

plt.bar(xpos, cols_small_Greedy, width=barWidth, label=subtitles[0])
plt.bar([x + 0.2 for x in xpos], cols_small_Ran, width=barWidth, label=subtitles[1])
plt.bar([x + 0.4 for x in xpos], cols_small_Genetic, width=barWidth, label=subtitles[3])

plt.xticks([x + 0.3 for x in xpos], ns)
plt.legend()

plt.title("Wykres zależności N od Liczby chromatycznej")
plt.xlabel("N")
plt.ylabel("Liczba Chromatyczna")

plt.show()
