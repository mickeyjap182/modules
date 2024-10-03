import os, sys, time, unittest

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# It is required when you'll run the unittest.
if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    if path not in sys.path:
        sys.path.append(path)
from tests.core import (
    Config
)

from ml.regression import (
    Simple
)

class SimpleRegressionTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_boston_dataset_analysys(self):
        """
        @see https://lib.stat.cmu.edu/datasets/boston

        """

        input_file = os.path.join(Config.test_path, 'ml', 'input', 'boston.csv')
        output = os.path.join(Config.test_path, 'ml', 'output')

        dataset = pd.read_csv(input_file, sep='\s+')

        # 前処理
        df = self.BostonDataset.filter_simple(dataset)
        """
        LSTAT    労働者階級の割合
        MEDV     所有者居住住宅の中央値（1000ドル単位）
        """
        df = df.filter(['LSTAT','MEDV'])

        print(df.shape)
        # 入力データ数
        N = df.shape[0]
        # 入力データの引数の数
        I = df.shape[1]
        lstat = df['LSTAT'].to_list()
        medv = df['MEDV'].to_list()
        # 散布図の描画
        self.BostonDataset.scatter_plot(lstat, medv, os.path.join(output, "simple_regression.png"))
        w = np.ones(2)
        # 単回帰
        model = Simple(N, 1000, 0.02)
        model.run(w, lstat, medv)
        self.assertTrue(True)

    class BostonDataset():
        """
 Variables in order:
 CRIM     per capita crime rate by town
            町ごとの犯罪発生率
 ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
            25000 平方フィートの敷地にある住宅区画の割合
 INDUS    proportion of non-retail business acres per town
            小売業以外のビジネスのエーカー割合
 CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
            チャーリー川ダミー値
 NOX      nitric oxides concentration (parts per 10 million)
            一酸化窒素濃度
 RM       average number of rooms per dwelling
            住宅あたりの平均部屋数
 AGE      proportion of owner-occupied units built prior to 1940
            1940年以前に建てられた所有者居住用区画の割合
 DIS      weighted distances to five Boston employment centres
            ボストンの5つの労働センターまでの距離の重み
 RAD      index of accessibility to radial highways
            放射状の高速道路へのアクセス指標
 TAX      full-value property-tax rate per $10,000
            10,000ドルあたりの固定資産税率
 PTRATIO  pupil-teacher ratio by town
            町あたりの生徒と教師の比率
 B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
            1000(Bk - 0.63)^2 (Bk:町ごとの黒人の割合)
 LSTAT    % lower status of the population
            労働者階級の割合
 MEDV     Median value of owner-occupied homes in $1000's        
            所有者居住住宅の中央値（1000ドル単位）
        """
        def __init__(self):
            pass

        @staticmethod
        def scatter_plot(x: list, y:list, graph_path:str ) -> None:
            plt.scatter(x, y)
            plt.savefig(graph_path)

        @staticmethod
        def filter_simple(dataset: pd.DataFrame) -> pd.DataFrame:
            """ 前処理サンプル """
            df = dataset.query("ZN >= 0.20 & ZN <= 95.00")
            return df

if __name__ == '__main__':
    unittest.main()
