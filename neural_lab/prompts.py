"""Utilities for predictable context and prompt assembly."""


def truncate_words(text: str, budget: int) -> str:
    """Approximate a context budget using whitespace-delimited words."""
    if budget < 0:
        raise ValueError("budget cannot be negative")
    words = text.split()
    return " ".join(words[:budget])


def build_context(system: str, memories: list[str], task: str, budget: int = 500) -> str:
    sections = [
        f"SYSTEM\n{system.strip()}",
        "MEMORY\n" + "\n".join(f"- {item}" for item in memories),
        f"TASK\n{task.strip()}",
    ]
    return truncate_words("\n\n".join(sections), budget)
