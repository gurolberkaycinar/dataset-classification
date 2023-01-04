# importing libraries
import pandas as pd
import sys
import matplotlib.pyplot as plt
from sklearn.linear_model import LassoCV
from pathlib import Path
from sklearn.linear_model import LinearRegression


def calculate_importance(dataset_name, label_column, type):
    dataset = pd.read_csv(str(Path(__file__).parent.parent.parent) + "/datasets/" + dataset_name + ".csv")

    X = dataset.drop(columns=[label_column])
    y = dataset[label_column]


    # reg = LassoCV()
    # reg.fit(X, y)
    # coef = pd.Series(reg.coef_)
    # print(coef)
    # coef = coef.sort_values()
    # coef.plot(kind="bar")
    # plt.title("Feature importances")
    # plt.tight_layout()
    # plt.savefig('graph.png')
    # plt.show()

    model = LinearRegression()
    # fit the model
    model.fit(X, y)
    # get importance
    importance = model.coef_
    # summarize feature importance
    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))
    # plot feature importance
    df = pd.DataFrame(data=X)
    plt.bar([df.head(n=1).columns[i] for i in range(len(importance))], importance)
    plt.xticks(rotation=90)
    plt.title("Feature importances")
    plt.savefig('graph.png')
    plt.tight_layout()
    plt.show()
    importance = importance.tolist()

    return importance