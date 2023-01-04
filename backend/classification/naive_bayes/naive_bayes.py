import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from pathlib import Path


def naive_bayes_train(file, label_column, test_percentage):
    X = file.drop(columns=[label_column])
    y = file[label_column]

    test_ratio = test_percentage / 100
    train_features, test_features, train_labels, test_answers = train_test_split(X, y, test_size=test_ratio)

    model = GaussianNB()
    model.fit(train_features, train_labels)

    predictions = model.predict(test_features)

    accuracy = accuracy_score(test_answers, predictions)
    precision = precision_score(test_answers, predictions, average='weighted')
    recall = recall_score(test_answers, predictions, average='weighted')

    # filtered predicter
    global filtered_naive_bayes
    filtered_naive_bayes = GaussianNB()
    new_dataset = pd.read_csv(str(Path(__file__).parent.parent.parent) + "/datasets/new_dataset_phishing.csv")
    X = new_dataset.drop(columns=[label_column])
    y = new_dataset[label_column]
    filtered_naive_bayes.fit(X, y)

    return accuracy, precision, recall


def naive_bayes_predict(features_dict: dict, label):
    features_dict.pop(label)
    features = pd.DataFrame.from_dict([features_dict])
    return filtered_naive_bayes.predict(features)
