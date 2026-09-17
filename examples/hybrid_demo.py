from neural_lab.hybrid import combine, rank


candidates = [
    combine("semantic memory for agents", semantic=0.94, lexical=0.35),
    combine("agent memory architecture", semantic=0.79, lexical=0.91),
    combine("image classification", semantic=0.22, lexical=0.04),
]

for item in rank(candidates):
    print(f"{item.score:.3f}  {item.text}")
