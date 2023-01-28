from typing import List

import numpy as np
import matplotlib.pyplot as plt

from wafermap_plot.models.defect_point import DefectPoint

from wafermap_plot.libs import color


class WaferMapPlot:
    @staticmethod
    def plot(defect_points: List[DefectPoint]) -> plt.Figure:

        x = np.linspace(-100, 100, 100)
        y = np.linspace(-100, 100, 100)

        X, Y = np.meshgrid(x, y)

        F = X**2 + Y**2 - 100 * 100

        fig, ax = plt.subplots()

        ax.contour(X, Y, F, [0], colors="black")
        ax.set_aspect(1)

        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        plt.xlim(-110, 110)
        plt.ylim(-110, 110)

        unique_bins = sorted(list(set(map(lambda x: x.bin, defect_points))))

        colors = color.generate_distinct_colors(len(unique_bins))

        for index, unique_bin in enumerate(unique_bins):
            tmp_defect_points = [
                dp.point for dp in defect_points if dp.bin == unique_bin
            ]

            ax.scatter(*zip(*tmp_defect_points), s=1, c=colors[index], marker="s")

        return fig
