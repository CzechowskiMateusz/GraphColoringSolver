import networkx as nx 
import matplotlib.pyplot as plt  
ns = [15, 20, 25, 30]

subtitles = ["Algorytm Zachłanny", "Algorytm Zachłanny Losowy", "Algorytm genetyczny"]
times__Greedy = [ 0.0000001232126,  0.0007231221231, 0.0009984970092773438, 0.06238590923790  ] 
times__Ran = [0.0000002239848, 2.000997304916381836, 4.09980201721191406, 7.231889279]
times__Genetic = [0.9933643341064453, 4.507972002029419, 139.029198, 721.12038 ]
 

# 100 100 0.1 = 79.9090
# 3 100 0.3 = 0.99

plt.plot(ns, times__Greedy, '-o')
plt.plot(ns, times__Ran, '-o')
plt.plot(ns, times__Genetic, '-o')

plt.legend(subtitles)

plt.title("Wykres zależności dużych danych testowych od czasu")
plt.xlabel("Data")
plt.ylabel("Time")
plt.grid(True)
plt.xticks(ns)
plt.show()
