import os
import numpy as np
import matplotlib.pyplot as plt

class Graph():
    def __init__(self, *args, **kwargs):
        """
        """
        self.fig, self.ax = plt.subplots()

    def new(self):
        """ new graph """
        return self.ax.twinx()

    def save(self, graph, path):
        graph.savefig(path)

    def draw(self, graph, size, data, **kwargs):
        if 'addtional' in kwargs and  kwargs.pop('addtional') == True :
            ax = self.new()
        else :
            ax = self.ax
        return graph.draw(ax, size, data, **kwargs)

class Line():
    """ line graph visualizer """
    def __init__(self, **kwargs):
        self.title = kwargs.pop('title') if 'title' in kwargs else None
        self.y_label = kwargs.pop('y_label') if 'y_label' in kwargs else 'untitled'
        self.grid = kwargs.pop('grid') if 'grid' in kwargs else False

    def draw(self, ax, size, data, **kwargs):
        left = np.array(size)
        height = np.array(data)
        ax.plot(left, height, **kwargs)
        if self.title is not None : ax.set_title(self.title)
        ax.grid(self.grid)
        ax.set_xlabel('days')
        ax.set_ylabel(self.y_label)

class Bar():
    """ Bar graph visualizer """
    def __init__(self, **kwargs):
        self.title = kwargs.pop('title') if 'title' in kwargs else None
        self.y_label = kwargs.pop('y_label') if 'y_label' in kwargs else 'untitled'

    def draw(self, ax, size, data, **kwargs):
        left = np.array(size)
        height = np.array(data)
        ax.bar(left, height, **kwargs)
        if self.title is not None : ax.set_title(self.title)
        ax.set_ylabel(self.y_label)
