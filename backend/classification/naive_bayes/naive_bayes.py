# Import LabelEncoder
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def naive_bayes(file):
    X = file.drop(columns=['Finishing'])  # select all columns except 'quality' as features
    y = file['Finishing']  # select 'quality' column as target variable

    train_features, test_features, train_labels, test_answers = train_test_split(X, y, test_size=0.99)

    model = GaussianNB()
    model.fit(train_features, train_labels)

    predictions = model.predict(test_features)

    accuracy = accuracy_score(test_answers, predictions)
    precision = precision_score(test_answers, predictions, average='weighted')
    recall = recall_score(test_answers, predictions, average='weighted')
    f1 = f1_score(test_answers, predictions, average='weighted')
    confusion = confusion_matrix(test_answers, predictions)

    print(f'Accuracy: {accuracy:.2f}')
    print(f'precision: {precision:.2f}')
    print(f'recall: {recall:.2f}')
    print(f'f1: {f1:.2f}')
    print(confusion)

    return accuracy, precision, recall, f1
