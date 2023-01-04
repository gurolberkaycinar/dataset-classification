# importing libraries
import base64

import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from sklearn.linear_model import LassoCV
from pathlib import Path
from sklearn.linear_model import LinearRegression

def filter_dataset(dataset_name, label_column):
    old_dataset = pd.read_csv(str(Path(__file__).parent.parent.parent) + "/datasets/" + dataset_name + ".csv")
    old_dataset['status'] = old_dataset['status'].replace(['legitimate'], '0')
    old_dataset['status'] = old_dataset['status'].replace(['phishing'], '1')
    df = pd.DataFrame(data=old_dataset)
    df = df.drop(['url'], axis=1)

    X = old_dataset.drop(columns=[label_column, "url"])
    y = old_dataset[label_column]

    model = LinearRegression()
    # fit the model
    model.fit(X, y)
    # get importance
    importance = model.coef_
    # summarize feature importance

    plt.bar([df.head(n=1).columns[i] for i in range(len(importance))], importance)
    plt.xticks(fontsize=5, rotation=90)
    plt.title("Unfiltered")
    plt.tight_layout()
    plt.savefig('old_graph.png', dpi=500)
    plt.close()

    indexes = np.array(importance)
    indexes = np.absolute(indexes)
    indexes = np.argpartition(indexes, -10)[-10:]
    indexes = indexes.tolist()

    ## Creating new data
    new_data = pd.DataFrame(df.iloc[:, indexes])
    new_data["status"] = y

    X = new_data.drop(labels="status", axis=1)
    y = new_data["status"]

    model.fit(X, y)
    # get importance
    importance = model.coef_

    plt.cla()
    plt.bar([new_data.head(n=1).columns[i] for i in range(len(importance))], importance)
    plt.xticks(fontsize=5, rotation=30)
    plt.title("Filtered")
    plt.tight_layout()
    plt.savefig('new_graph.png', dpi=500)
    plt.close()
    # plt.show()

    new_data.to_csv(str(Path(__file__).parent.parent.parent) + '/datasets/new_' + dataset_name + '.csv')