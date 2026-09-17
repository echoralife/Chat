"""Text chunking primitives for retrieval pipelines."""


def chunk_words(text: str, size: int = 120, overlap: int = 20) -> list[str]:
    if size <= 0:
        raise ValueError("size must be positive")
    if overlap < 0 or overlap >= size:
        raise ValueError("overlap must satisfy 0 <= overlap < size")
    words = text.split()
    step = size - overlap
    return [" ".join(words[i : i + size]) for i in range(0, len(words), step) if words[i : i + size]]
