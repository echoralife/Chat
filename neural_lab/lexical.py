"""Tiny lexical retrieval utilities."""

import math
import re
from collections import Counter


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def tfidf_score(query: str, document: str, corpus: list[str]) -> float:
    q = Counter(tokenize(query))
    d = Counter(tokenize(document))
    if not q or not d:
        return 0.0
    score = 0.0
    for term in q:
        containing = 1 + sum(term in set(tokenize(item)) for item in corpus)
        idf = math.log((1 + len(corpus)) / containing) + 1
        score += d[term] * idf
    return score / max(sum(d.values()), 1)
