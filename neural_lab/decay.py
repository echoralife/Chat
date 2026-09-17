"""Recency weighting for long-lived agent memories."""

import math


def exponential_decay(age_hours: float, half_life_hours: float = 72.0) -> float:
    if age_hours < 0:
        raise ValueError("age cannot be negative")
    if half_life_hours <= 0:
        raise ValueError("half life must be positive")
    return math.exp(-math.log(2) * age_hours / half_life_hours)


def weighted_score(relevance: float, age_hours: float, recency_weight: float = 0.2) -> float:
    if not 0 <= recency_weight <= 1:
        raise ValueError("recency_weight must be between zero and one")
    return (1 - recency_weight) * relevance + recency_weight * exponential_decay(age_hours)
