from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt


class Scatter3D:
    def __init__(self, x_label="", y_label="", z_label=""):
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig)

        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.set_zlabel(z_label)

    def plot_point(self, x, y, z):
        self.ax.scatter(x, y, z)

    def plot_data(self, x_data, y_data, z_data):
        self.ax.scatter(x_data, y_data, z_data)

    def plot_points(self, points):
        for p in points:
            self.plot_point(*p)

    def show(self):
        plt.show()
