import hashlib

from neural_lab import TinyAgent, VectorMemory


def toy_embed(text: str) -> list[float]:
    """Deterministic local embedding for demos; not a semantic model."""
    digest = hashlib.sha256(text.lower().encode()).digest()
    return [byte / 255 for byte in digest[:8]]


agent = TinyAgent(VectorMemory(8), toy_embed)
agent.observe("The cache uses a least-recently-used eviction policy.")
agent.observe("Agent memories are ranked before entering the prompt.")
agent.observe("Evaluation should be deterministic when possible.")

print(agent.context("How does memory enter the agent context?", limit=2))
