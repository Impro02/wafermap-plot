import random
from typing import List, Tuple

from sklearn.metrics.pairwise import euclidean_distances


def random_rgb_color() -> Tuple[int, int, int]:
    return (random.randint(0, 255) for _ in range(3))


def convert_rgb_hex(rgb: Tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


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
