from math import sqrt
from typing import List


def mean(value_list: List[float]) -> float:
    return float(sum(value_list) / len(value_list))


def variance(value_list: List[float], ddof: int = 0) -> float:
    mean_list = mean(value_list)
    return float(sum((value - mean_list) ** 2 for value in value_list) / (len(value_list) - ddof))


def stddev(value_list: List[float]) -> float:
    return sqrt(variance(value_list))


def median(value_list: List[float]) -> float:
    sorted_list = sorted(value_list)
    len_list = len(sorted_list)
    index_middle = int(len_list/2)

    if len_list % 2 == 0:
        return float((sorted_list[index_middle-1]+sorted_list[index_middle])/2)
    else:
        return float(sorted_list[index_middle])

