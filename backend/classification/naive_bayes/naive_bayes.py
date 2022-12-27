# Import LabelEncoder
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

model = GaussianNB()

def naive_bayes_train(file, label_column, test_percentage):
    X = file.drop(columns=[label_column])  # select all columns except 'quality' as features
    y = file[label_column]  # select 'quality' column as target variable

    test_ratio = test_percentage / 100
    train_features, test_features, train_labels, test_answers = train_test_split(X, y, test_size=test_ratio)

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

def naive_bayes_predict(features):
    prediction = model.predict(features)
    # print(f'Prediction: {prediction:.2f}')
    return prediction