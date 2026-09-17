from neural_lab.memory import VectorMemory


memory = VectorMemory(dimensions=3)
memory.add("Attention lets a model weight relevant tokens.", [0.95, 0.20, 0.10])
memory.add("Vector databases support similarity search.", [0.70, 0.65, 0.20])
memory.add("Gradient descent optimizes model parameters.", [0.30, 0.10, 0.95])

for result in memory.search([0.85, 0.35, 0.10], limit=2):
    print(f"{result.score:.3f}  {result.text}")
