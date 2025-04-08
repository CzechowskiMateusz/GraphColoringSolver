import networkx as nx 
import matplotlib.pyplot as plt  
ns = [3,4,5,6,7,8]

subtitles = ["Algorytm Zachłanny", "Algorytm Zachłanny Losowy", "Algorytm siłowy", "Algorytm genetyczny"]
times_small_Greedy = [0.0, 0.0000123132, 0.0,  0.0000213123484, 0.0, 0.000131020320, ]
times_small_Ran = [0.0009927749633789062, 0.0012994304322, 0.000992123, 0.001003265380859375, 0.0, 0.0002318877678235]
times_small_Full = [0.0009951591491699219, 0.01000213623046875, 0.3650245666503906 , 6.606289863586426, 448.44522166252136  ,536.3857476711273]
times_small_Genetic = [0.15860748291015625, 0.4059426784515381, 0.32515764236450195, 1.3952679634094238, 0.9025864601135254,  2.3527371883392334]

plt.plot(ns, times_small_Greedy, '-o')
plt.plot(ns, times_small_Ran, '-o')
plt.plot(ns, times_small_Full, '-o')
plt.plot(ns, times_small_Genetic, '-o')

plt.legend(subtitles)

plt.title("Wykres zależności małych danych testowych od czasu")
plt.xlabel("Data")
plt.ylabel("Time")
plt.grid(True)
plt.xticks(ns)
plt.show()
