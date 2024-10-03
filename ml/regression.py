import pandas as pd
import numpy as np
from logging import getLogger

logger = getLogger(__name__)
class Simple() :
    """
        単回帰モデル simple regression
    """
    def __init__(self, data_cnt, repetition, rate):
        # データ数　data_cnt
        self.data_cnt = data_cnt
        # 学習回数　repetition
        self.repetition = repetition
        # 学習率　rate
        self.rate = rate

    def run(self, w, x, yt):
        print(w)
        print(x)
        print(yt)

        evaluation = np.zeros((0,2 ))
        print(evaluation)
        logger.info("start evaluation.")
        for k in range(self.repetition):
            yp = self.predict(k, w)

            err = yp - yt

            w = w - rate * (x.T @ err) / self.data_cnt

            if (k % 100 == 0) :
                loss = np.mean(err ** 2) / 2
                evaluation = np.vstack((history, np.array))

    def predict(self, x, w):
        return x @ w




class Multiple() :
    def __init__(self, dataset:pd):
        pass

    def run(self):
        pass
