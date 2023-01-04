# Import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import pandas as pd



def knn_train(file, label_column, test_percentage, neighbors, distance_power):
    X = file.drop(columns=[label_column])
    y = file[label_column]
    test_ratio = test_percentage / 100

    train_features, test_features, train_labels, test_answers = train_test_split(X, y, test_size=test_ratio)

    global knn
    knn = KNeighborsClassifier(n_neighbors=neighbors, p=distance_power)
    knn.fit(train_features, train_labels)

    predictions = knn.predict(test_features)

    accuracy = accuracy_score(test_answers, predictions)
    precision = precision_score(test_answers, predictions, average='weighted')
    recall = recall_score(test_answers, predictions, average='weighted')

    confusion = confusion_matrix(test_answers, predictions)

    print(f'Accuracy: {accuracy:.2f}')
    print(f'precision: {precision:.2f}')
    print(f'recall: {recall:.2f}')
    print(confusion)

    return accuracy, precision, recall


def knn_predict(features_dict: dict, label):
    features_dict.pop(label)
    features = pd.DataFrame.from_dict([features_dict])
    return knn.predict(features)
