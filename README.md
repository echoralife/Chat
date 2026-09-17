# Neural Lab

A compact AI engineering playground for experimenting with retrieval, agent memory, embeddings, evaluation, and small autonomous systems.

> Built as a collection of readable, dependency-light experiments rather than a single monolithic framework.

## Overview

Neural Lab contains small modules that explore common building blocks behind modern AI systems:

- **Semantic memory** — cosine-similarity retrieval over vector memories
- **Agent loops** — minimal perceive → retrieve → decide → remember cycles
- **Evaluation** — lightweight metrics for ranking and retrieval quality
- **Prompt utilities** — structured prompt assembly and context budgeting
- **Synthetic data** — deterministic generators for testing AI pipelines

## Repository structure

```text
.
├── neural_lab/
│   ├── agent.py
│   ├── memory.py
│   ├── prompts.py
│   └── evaluation.py
├── examples/
├── tests/
├── docs/
├── pyproject.toml
└── README.md
```

## Quick start

Requires Python 3.10+.

```bash
git clone https://github.com/echoralife/Chat.git
cd Chat
pip install -e .
python examples/memory_demo.py
```

## Example

```python
from neural_lab.memory import VectorMemory

memory = VectorMemory(dimensions=3)
memory.add("transformers use attention", [0.9, 0.2, 0.1])
memory.add("databases persist structured records", [0.1, 0.8, 0.3])

results = memory.search([0.8, 0.2, 0.1], limit=1)
print(results[0].text)
```

## Design principles

**Small primitives.** Components should be useful independently.

**Transparent behavior.** Important logic stays visible instead of being hidden behind large frameworks.

**Deterministic tests.** Core experiments run without network access or API keys.

**Composable systems.** Memory, prompting, evaluation, and agent logic use simple interfaces so they can be recombined.

## Roadmap

- Hybrid lexical + vector retrieval
- Persistent SQLite memory backend
- Tool-routing experiments
- Agent trajectory tracing
- Retrieval benchmarks
- Context compression strategies
- Multi-agent message passing

## License

MIT
