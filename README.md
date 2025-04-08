# 🎨 GraphColoringSolver

A Python-based tool for solving the graph coloring problem using multiple algorithms, including greedy, random, and metaheuristic (genetic) approaches.

## 📌 About

This project compares different graph coloring strategies by evaluating their efficiency and effectiveness on sample input data. It uses various algorithms to determine the chromatic number of a graph and stores the results for further analysis.

### Algorithms Implemented:
- 🟢 **Greedy** – Fast, simple heuristic
- 🎲 **Randomized** – Greedy with random choices
- 🧠 **Genetic Algorithm** – Metaheuristic optimization
- 🧪 **Brute Force (Full)** – (Optional showcase only)

## 📁 Project Structure
GraphColoringSolver/ 
│ ├── codes/ 
│ ├── write_graphs.py # Visualization and graph drawing 
│ ├── greedy_algorithm.py # Greedy algorithm logic 
│ ├── random_algorithm.py # Randomized greedy logic 
│ ├── full_algorithm.py # Brute-force solution (optional) 
│ └── metaheuristic.py # Genetic algorithm implementation 
│ ├── test_data/ │ └── data_v15.json # Sample input graph (adjacency matrix + vertices) 
│ ├── result_data/ │ └── data_v15_greedy.json # Output of greedy algorithm 
│ └── data_v15_random.json # Output of randomized algorithm 
│ └── data_v15_genetic.json # Output of genetic algorithm 
│ └── main.py # Runner script for all algorithms


## ⚙️ How to Run

### Prerequisites

- Python 3.8+
- Install required packages:
```bash
pip install matplotlib
