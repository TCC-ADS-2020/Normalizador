import numpy as np


def normalizer(array):
    min_value = np.min(array)
    max_value = np.max(array)

    difference = np.subtract(array, min_value)
    normalized = np.divide(difference, (max_value - min_value))

    return normalized
