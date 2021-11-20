from math import sqrt
from typing import List


def mean(value_list: List[float]) -> float:
    return sum(value_list) / len(value_list)


def variance(value_list: List[float], ddof: int = 0) -> float:
    mean_list = mean(value_list)
    return sum((value - mean_list) ** 2 for value in value_list) / (len(value_list) - ddof)


def stddev(value_list: List[float]) -> float:
    return sqrt(variance(value_list))


