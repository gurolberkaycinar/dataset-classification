#importing libraries
import pandas as pd
import sys
import matplotlib.pyplot as plt
from sklearn.linear_model import LassoCV
from pathlib import Path

def calculate_importance(dataset_name, label_column):
    print(Path(__file__).parent.parent.parent)
    dataset = pd.read_csv(str(Path(__file__).parent.parent.parent) + "/datasets/" + dataset_name + ".csv", usecols=lambda x: x != 'url')
    X = dataset.drop(columns=[label_column])
    y = dataset[label_column]

    reg = LassoCV()
    reg.fit(X, y)
    coef = pd.Series(reg.coef_, index=X.columns)
    coef = coef.sort_values()
    print("plotting")
    coef.plot(kind="bar")
    plt.show()
    plt.title("Feature importances")
    return coef
