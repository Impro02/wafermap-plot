import random
from typing import List


from sklearn.metrics.pairwise import euclidean_distances

import numpy as np


def random_rgb_color():
    # return np.random.randint(0, 255, size=(3,))
    return [random.randint(0, 255) for _ in range(3)]


def convert_rgb_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def delta_E_CIE1976(Lab1, Lab2):
    return np.linalg.norm(np.array(Lab1) - np.array(Lab2))


def generate_distinct_colors(nbr_colors: int) -> List[str]:
    colors = [[0, 0, 0]]
    while len(colors) < nbr_colors:
        tmp_color = random_rgb_color()

        is_similar = any(
            [euclidean_distances([tmp_color], [color]) < 50.0 for color in colors]
        )

        if not is_similar:
            colors.append(tmp_color)

        continue

    return [convert_rgb_hex(color) for color in colors]
