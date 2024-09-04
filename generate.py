import os
import numpy as np
import matplotlib.pyplot as plt


path = os.path.join(os.path.dirname(__file__), 'height.txt')
xs = np.loadtxt(path)

sigma = np.std(xs)#標準偏差




def generate_height(mu):
    samples = np.random.normal(mu, sigma, 1000000)#mu,sigmaの正規分布に従う値をランダムに10000個選び取る　ここで生成しているということ

    plt.hist(samples, bins='auto', density=True, alpha = 0.7, label='original')
    plt.legend()
    plt.show()

generate_height(200)#この引数は身長のスケールが違う人類？のような身長の分布にすることができるってこと



